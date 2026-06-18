<template>
  <main class="keywords-page">
    <!-- 流式背景视频 -->
    <SubpageBgVideo
      src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260525_052706_d2e390fd-1846-4fe7-a4d8-8d2f1c875358.mp4" />

    <!-- 头部导航栏 -->
    <LibraryTopNav v-model:search="search" />

    <!-- 页面核心包围壳 -->
    <div class="keywords-shell">
      <!-- 1. 顶部数据统计看板 -->
      <KeywordHeader class="keywords-motion reveal-header" :total-keywords="totalKeywords" :avg-keywords="avgKeywords"
        :top-keywords="topKeywords" />

      <!-- 2. 特征词云展示区 -->
      <KeywordCloud class="keywords-motion reveal-cloud" :keywords="keywordsList" :active-keyword="activeKeyword"
        @select-keyword="handleKeywordSelect" />

      <!-- 3. 关联透视数据看板 -->
      <KeywordDashboard class="keywords-motion reveal-dashboard" :keyword="activeKeyword"
        :doc-count="dashboardData.docCount" :risk-levels="dashboardData.riskLevels"
        :business-stages="dashboardData.businessStages" :categories="dashboardData.categories" />

      <!-- 4. 关联文献资料卡片列表 -->
      <KeywordRelatedList class="keywords-motion reveal-list" :keyword="activeKeyword" :docs="relatedDocs" />
    </div>

    <!-- 底部页脚 -->
    <LibraryFooter />
  </main>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue'
import docs from '../data/complianceDocs.json'

// 导入公共组件
import LibraryTopNav from '../components/gonggongzujian/LibraryTopNav.vue'
import SubpageBgVideo from '../components/gonggongzujian/SubpageBgVideo.vue'
import LibraryFooter from '../components/library/LibraryFooter.vue'

// 导入关键词子组件
import KeywordHeader from '../components/keywords/KeywordHeader.vue'
import KeywordCloud from '../components/keywords/KeywordCloud.vue'
import KeywordDashboard from '../components/keywords/KeywordDashboard.vue'
import KeywordRelatedList from '../components/keywords/KeywordRelatedList.vue'

const search = ref('')
const activeKeyword = ref('')

// --- 数据统计与清洗逻辑 ---

// 统计所有去重后的关键词及出现次数
const keywordsList = computed(() => {
  const map = {}
  docs.forEach(doc => {
    if (doc.keywords && Array.isArray(doc.keywords)) {
      doc.keywords.forEach(kw => {
        map[kw] = (map[kw] || 0) + 1
      })
    }
  })
  return Object.entries(map).map(([name, count]) => ({ name, count }))
})

// 特征词唯一总数
const totalKeywords = computed(() => keywordsList.value.length)

// 最常出现特征词排行（前3名）
const topKeywords = computed(() => {
  return [...keywordsList.value]
    .sort((a, b) => b.count - a.count)
    .slice(0, 3)
})

// 平均每篇文献的特征词数量
const avgKeywords = computed(() => {
  if (!docs.length) return '0.0'
  const total = docs.reduce((sum, doc) => sum + (doc.keywords ? doc.keywords.length : 0), 0)
  return (total / docs.length).toFixed(1)
})

// --- 激活关键词关联数据逻辑 ---

// 关联当前选中关键词的所有合规文献
const relatedDocs = computed(() => {
  if (!activeKeyword.value) return []
  return docs.filter(doc => doc.keywords && doc.keywords.includes(activeKeyword.value))
})

// 动态计算该关键词在其他维度的占比分布
const dashboardData = computed(() => {
  if (!activeKeyword.value || !relatedDocs.value.length) {
    return {
      docCount: 0,
      riskLevels: { 高: 0, 中: 0, 低: 0 },
      businessStages: [],
      categories: []
    }
  }

  const list = relatedDocs.value
  const riskLevels = { 高: 0, 中: 0, 低: 0 }
  const stagesMap = {}
  const catsMap = {}

  list.forEach(doc => {
    // 1. 风险统计
    if (doc.riskLevel in riskLevels) {
      riskLevels[doc.riskLevel]++
    } else {
      // 容错处理
      riskLevels[doc.riskLevel] = 1
    }

    // 2. 业务阶段统计
    if (doc.businessStage) {
      stagesMap[doc.businessStage] = (stagesMap[doc.businessStage] || 0) + 1
    }

    // 3. 政策主题类别统计
    if (doc.category) {
      catsMap[doc.category] = (catsMap[doc.category] || 0) + 1
    }
  })

  // 转化为数组并按次数降序排列
  const businessStages = Object.entries(stagesMap)
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => b.count - a.count)

  const categories = Object.entries(catsMap)
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => b.count - a.count)

  return {
    docCount: list.length,
    riskLevels,
    businessStages,
    categories
  }
})

// 点击选择词云标签
const handleKeywordSelect = (kw) => {
  activeKeyword.value = kw
}

// --- 渐显入场动效控制 ---
const observedElements = new WeakSet()
let revealObserver

const setupKeywordsMotion = () => {
  if (typeof window === 'undefined') return
  const targets = document.querySelectorAll('.keywords-page .keywords-motion')
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  const canObserve = 'IntersectionObserver' in window

  if (reduceMotion || !canObserve) {
    targets.forEach(el => el.classList.add('is-visible'))
    return
  }

  if (!revealObserver) {
    revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible')
            revealObserver?.unobserve(entry.target)
          }
        })
      },
      {
        threshold: 0.08,
        rootMargin: '100px 0px 100px 0px'
      }
    )
  }

  targets.forEach(el => {
    if (!(el instanceof HTMLElement) || observedElements.has(el)) return
    observedElements.add(el)
    revealObserver.observe(el)
  })
}

onMounted(async () => {
  await nextTick()
  setupKeywordsMotion()

  // 默认选中频次最高的一个关键词，让页面一进来就有些内容展示，体验更好
  if (topKeywords.value.length > 0) {
    activeKeyword.value = topKeywords.value[0].name
  }
})

onBeforeUnmount(() => {
  revealObserver?.disconnect()
})
</script>

<style scoped>
.keywords-page {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  color: var(--color-text, #ffffff);
}

/* 渐变星空微粒背景效果 */
.keywords-page::before {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.012) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.012) 1px, transparent 1px);
  background-size: 80px 80px;
  mask-image: linear-gradient(180deg, #000 0%, rgba(0, 0, 0, 0.76) 50%, transparent 100%);
  content: '';
}

.keywords-shell {
  position: relative;
  z-index: 1;
  width: min(1440px, calc(100% - 48px));
  margin: 0 auto;
  padding: clamp(60px, 8vw, 100px) 0 92px;
}

/* 动效入场初始状态 */
.keywords-motion {
  opacity: 0;
  filter: blur(8px);
  transform: translate3d(0, 26px, 0) scale(0.99);
  transition:
    opacity 0.76s var(--ease-premium),
    filter 0.76s var(--ease-premium),
    transform 0.76s var(--ease-premium);
  will-change: opacity, filter, transform;
}

.keywords-motion.is-visible {
  opacity: 1;
  filter: blur(0);
  transform: translate3d(0, 0, 0) scale(1);
}

.reveal-header {
  transition-delay: 50ms;
}

.reveal-cloud {
  transition-delay: 150ms;
}

.reveal-dashboard {
  transition-delay: 250ms;
}

.reveal-list {
  transition-delay: 350ms;
}

@media (max-width: 700px) {
  .keywords-shell {
    width: min(1440px, calc(100% - 32px));
  }
}
</style>
