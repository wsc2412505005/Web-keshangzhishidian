<template>
  <main class="library-page">
    <SubpageBgVideo src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260325_094440_a3592600-bd1e-49e5-9bce-a73662061d83.mp4" />
    <LibraryTopNav v-model:search="search" />

    <section class="library-shell">
      <LibrarySidebar
        class="library-motion reveal-sidebar"
        :categories="categories"
        :active-category="activeCategory"
        :insight="insight"
        @select-category="selectCategory"
      />

      <section class="library-content library-motion reveal-content" aria-label="合规文献列表">
        <LibraryToolbar
          class="library-motion reveal-toolbar"
          :total="normalizedDocs.length"
          :filtered-total="filteredDocs.length"
          :active-label="activeCategoryConfig.label"
          :sort-order="sortOrder"
          @reset="resetFilters"
          @toggle-sort="toggleSort"
        />

        <label class="mobile-search library-motion reveal-mobile-search">
          <span>搜索合规文本</span>
          <input v-model="search" type="search" placeholder="搜索标题、关键词、地区或风险..." />
        </label>

        <div v-if="pagedDocs.length" :key="'list-' + listMotionKey" class="document-list">
          <div
            v-for="(doc, index) in pagedDocs"
            :key="doc.id"
            class="document-motion-item library-motion reveal-document"
            :style="{ '--library-delay': `${Math.min(index * 92, 260)}ms` }"
          >
            <LibraryCard :doc="doc" :expanded="expandedId === doc.id" @toggle-detail="toggleDetail" />
          </div>
        </div>

        <section v-else :key="'empty-' + listMotionKey" class="empty-state library-motion reveal-document">
          <h2>没有找到匹配文本</h2>
          <p>可以换一个关键词，或者点击 Filter 回到全部资料。</p>
          <button type="button" @click="resetFilters">查看全部资料</button>
        </section>

        <LibraryPagination
          class="library-motion reveal-pagination"
          :current-page="currentPage"
          :total-pages="totalPages"
          @change="setPage"
        />
      </section>
    </section>

    <span id="classification" class="anchor-target"></span>
    <span id="keyword-analysis" class="anchor-target"></span>
    <LibraryFooter />
  </main>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import docs from '../data/complianceDocs.json'
import LibraryCard from '../components/library/LibraryCard.vue'
import LibraryFooter from '../components/library/LibraryFooter.vue'
import LibraryPagination from '../components/library/LibraryPagination.vue'
import LibrarySidebar from '../components/library/LibrarySidebar.vue'
import LibraryToolbar from '../components/library/LibraryToolbar.vue'
import LibraryTopNav from '../components/gonggongzujian/LibraryTopNav.vue'
import SubpageBgVideo from '../components/gonggongzujian/SubpageBgVideo.vue'

const route = useRoute()
const search = ref(route.query.search || '')
const activeCategory = ref('all')
const sortOrder = ref('desc')
const currentPage = ref(1)
const expandedId = ref(null)
const pageSize = 3
const observedMotionElements = new WeakSet()
let libraryRevealObserver

watch(
  () => route.query.search,
  (newSearch) => {
    search.value = newSearch || ''
  },
)

const categoryDefinitions = [
  {
    key: 'all',
    label: '全部文献',
    match: () => true,
  },
  {
    key: 'policy',
    label: '政策法规',
    match: (doc) => doc.sourceType.includes('政策') || doc.sourceType === '法律法规',
  },
  {
    key: 'news',
    label: '行业动态',
    match: (doc) => doc.sourceType.includes('新闻'),
  },
  {
    key: 'corporate',
    label: '企业公告',
    match: (doc) => doc.sourceType.includes('企业'),
  },
  {
    key: 'mining',
    label: '矿业合规专题',
    match: (doc) =>
      ['环保', '供应链', '外汇', '关税', '数据'].some(
        (keyword) => doc.category.includes(keyword) || doc.keywords.join('').includes(keyword),
      ),
  },
  {
    key: 'cross-border',
    label: '跨境投资布局',
    match: (doc) => ['总部布局', '投资设立', '跨境结算', '海外贸易'].some((stage) => doc.businessStage.includes(stage)),
  },
  {
    key: 'esg',
    label: 'ESG与绿色贸易',
    match: (doc) =>
      ['ESG', '环保', '碳', 'CBAM', '社区'].some(
        (keyword) => doc.category.includes(keyword) || doc.keywords.join('').includes(keyword),
      ),
  },
]

const displayTypeMap = {
  政策文件: '政策文件',
  政策解读: '政策解读',
  法律法规: '法律法规',
  行业新闻: '行业新闻',
  企业新闻: '企业新闻',
  企业报告: '企业报告',
  国际规则: '国际规则',
}

const normalizedDocs = computed(() =>
  docs.map((doc) => ({
    ...doc,
    displayType: displayTypeMap[doc.sourceType] || doc.sourceType,
    tone: resolveTone(doc),
    tags: doc.keywords.slice(0, 3),
    keywordPreview: doc.keywords.slice(0, 4).join(', '),
    dateLabel: doc.publishDate,
    searchableText: [
      doc.title,
      doc.sourceType,
      doc.region,
      doc.country,
      doc.businessStage,
      doc.category,
      doc.riskLevel,
      doc.summary,
      doc.excerpt,
      doc.analysis,
      doc.sourceName,
      ...doc.keywords,
    ]
      .join(' ')
      .toLowerCase(),
  })),
)

const categories = computed(() =>
  categoryDefinitions.map((category) => ({
    ...category,
    count: normalizedDocs.value.filter(category.match).length,
  })),
)

const activeCategoryConfig = computed(
  () => categories.value.find((category) => category.key === activeCategory.value) || categories.value[0],
)

const filteredDocs = computed(() => {
  const query = search.value.trim().toLowerCase()

  return normalizedDocs.value
    .filter((doc) => activeCategoryConfig.value.match(doc))
    .filter((doc) => !query || doc.searchableText.includes(query))
    .sort((left, right) => {
      const leftTime = new Date(left.publishDate).getTime()
      const rightTime = new Date(right.publishDate).getTime()
      return sortOrder.value === 'desc' ? rightTime - leftTime : leftTime - rightTime
    })
})

const totalPages = computed(() => Math.max(1, Math.ceil(filteredDocs.value.length / pageSize)))

const pagedDocs = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  return filteredDocs.value.slice(start, start + pageSize)
})

const listMotionKey = computed(() =>
  [activeCategory.value, sortOrder.value, currentPage.value, search.value.trim()].join('|'),
)

const insight = computed(() => ({
  total: normalizedDocs.value.length,
  sourceTypes: new Set(normalizedDocs.value.map((doc) => doc.sourceType)).size,
  highRisk: normalizedDocs.value.filter((doc) => doc.riskLevel === '高').length,
}))

watch([search, activeCategory, sortOrder], () => {
  currentPage.value = 1
  expandedId.value = null
})

watch(totalPages, (value) => {
  if (currentPage.value > value) {
    currentPage.value = value
  }
})

watch(
  listMotionKey,
  async () => {
    await nextTick()
    setupLibraryMotion()
  },
  { flush: 'post' },
)

onMounted(async () => {
  await nextTick()
  setupLibraryMotion()
})

onBeforeUnmount(() => {
  libraryRevealObserver?.disconnect()
})

function resolveTone(doc) {
  const keywordText = `${doc.category}${doc.keywords.join('')}`

  if (keywordText.includes('数据')) return 'data'
  if (['ESG', '环保', '碳', 'CBAM'].some((keyword) => keywordText.includes(keyword))) return 'esg'
  if (doc.sourceType === '国际规则') return 'global'
  if (doc.sourceType.includes('企业')) return 'corporate'
  if (doc.sourceType.includes('新闻')) return 'news'
  return 'policy'
}

function selectCategory(categoryKey) {
  activeCategory.value = categoryKey
}

function toggleSort() {
  sortOrder.value = sortOrder.value === 'desc' ? 'asc' : 'desc'
}

function resetFilters() {
  activeCategory.value = 'all'
  search.value = ''
}

function setPage(page) {
  currentPage.value = Math.min(Math.max(page, 1), totalPages.value)
  expandedId.value = null
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  })
}

function toggleDetail(id) {
  expandedId.value = expandedId.value === id ? null : id
}

function setupLibraryMotion() {
  if (typeof window === 'undefined') return

  const targets = document.querySelectorAll('.library-page .library-motion')
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  const canObserve = 'IntersectionObserver' in window

  if (reduceMotion || !canObserve) {
    targets.forEach((element) => element.classList.add('is-visible'))
    return
  }

  if (!libraryRevealObserver) {
    libraryRevealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return
          entry.target.classList.add('is-visible')
          libraryRevealObserver?.unobserve(entry.target)
        })
      },
      {
        threshold: 0.12,
        rootMargin: '80px 0px 80px 0px',
      },
    )
  }

  targets.forEach((element) => {
    if (!(element instanceof HTMLElement) || observedMotionElements.has(element)) return
    observedMotionElements.add(element)
    libraryRevealObserver.observe(element)
  })
}
</script>

<style scoped>
.library-page {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  color: var(--color-text);
}

.library-page::before {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 76px 76px;
  mask-image: linear-gradient(180deg, #000 0%, rgba(0, 0, 0, 0.72) 42%, transparent 100%);
  content: '';
}

.library-page::after {
  position: fixed;
  inset: -12% -18%;
  z-index: 0;
  pointer-events: none;
  background:
    linear-gradient(112deg, transparent 18%, rgba(200, 168, 102, 0.055) 45%, transparent 66%),
    radial-gradient(circle at 72% 18%, rgba(255, 255, 255, 0.035), transparent 24%);
  opacity: 0.22;
  transform: translate3d(-8%, -3%, 0);
  animation: library-ambient 15s var(--ease-premium) infinite alternate;
  content: '';
}

.library-shell {
  position: relative;
  z-index: 1;
  display: flex;
  width: min(1440px, calc(100% - 48px));
  margin: 0 auto;
  gap: clamp(38px, 5vw, 72px);
  padding: clamp(54px, 7vw, 92px) 0 92px;
}

.library-content {
  min-width: 0;
  flex: 1;
}

.document-list {
  display: grid;
  gap: 24px;
}

.document-motion-item {
  min-width: 0;
}

.library-motion {
  opacity: 0;
  filter: blur(8px);
  transform: translate3d(0, 24px, 0) scale(0.99);
  transition:
    opacity 0.74s var(--ease-premium),
    filter 0.74s var(--ease-premium),
    transform 0.74s var(--ease-premium);
  transition-delay: var(--library-delay, 0ms);
  will-change: opacity, filter, transform;
}

.library-motion.is-visible {
  opacity: 1;
  filter: blur(0);
  transform: translate3d(0, 0, 0) scale(1);
}

.reveal-sidebar {
  --library-delay: 60ms;

  transform: translate3d(-26px, 18px, 0) scale(0.99);
}

.reveal-content {
  --library-delay: 120ms;
}

.reveal-toolbar {
  --library-delay: 160ms;

  transform: translate3d(0, 18px, 0);
}

.reveal-mobile-search {
  --library-delay: 180ms;
}

.reveal-document {
  transform: translate3d(0, 34px, 0) scale(0.982);
}

.reveal-pagination {
  --library-delay: 120ms;

  transform: translate3d(0, 16px, 0) scale(0.99);
}

.mobile-search {
  display: none;
}

.empty-state {
  padding: 42px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.03);
}

.empty-state h2 {
  margin: 0;
  color: var(--color-text);
}

.empty-state p {
  margin: 10px 0 24px;
  color: var(--color-muted);
}

.empty-state button {
  min-height: 44px;
  padding: 0 18px;
  border: 0;
  border-radius: 999px;
  background: #ffffff;
  color: #090d16;
  cursor: pointer;
  font-weight: 900;
  transition:
    background 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}

.empty-state button:hover {
  background: #f2efe6;
  transform: translateY(-1px);
}

.anchor-target {
  position: relative;
  top: -80px;
  display: block;
  width: 1px;
  height: 1px;
}

@media (max-width: 980px) {
  .library-shell {
    display: grid;
    width: min(1440px, calc(100% - 32px));
    gap: 34px;
    padding-top: 40px;
  }

  .library-content {
    overflow: hidden;
  }
}

@media (max-width: 700px) {
  .mobile-search {
    display: grid;
    gap: 8px;
    margin: 0 0 22px;
    color: rgba(245, 239, 226, 0.54);
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 0.06em;
  }

  .mobile-search input {
    width: 100%;
    min-height: 46px;
    border: 1px solid rgba(245, 239, 226, 0.12);
    border-radius: 999px;
    outline: none;
    background: rgba(245, 239, 226, 0.055);
    color: var(--color-text);
    padding: 0 18px;
    transition:
      border-color 0.3s var(--ease-premium),
      background 0.3s var(--ease-premium),
      transform 0.3s var(--ease-premium);
  }

  .mobile-search input:focus {
    border-color: rgba(200, 168, 102, 0.55);
    background: rgba(245, 239, 226, 0.08);
    transform: translateY(-1px);
  }
}

@keyframes library-ambient {
  from {
    opacity: 0.16;
    transform: translate3d(-10%, -4%, 0);
  }

  to {
    opacity: 0.34;
    transform: translate3d(8%, 3%, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .library-page::after {
    animation: none;
  }

  .library-motion {
    opacity: 1;
    filter: none;
    transform: none;
    transition: none;
  }

  .mobile-search input,
  .empty-state button {
    transition: none;
  }
}
</style>
