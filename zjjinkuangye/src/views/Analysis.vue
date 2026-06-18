<template>
  <main class="analysis-page">
    <!-- 流式背景视频 -->
    <SubpageBgVideo
      src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260403_050628_c4e32401-fab4-4a27-b7a8-6e9291cd5959.mp4" />

    <!-- 头部导航栏 -->
    <LibraryTopNav v-model:search="search" />

    <!-- 驾驶舱核心包围壳 -->
    <div class="analysis-shell">
      <!-- 1. 顶部引言及核心指标指标卡 -->
      <AnalysisHero class="analysis-motion reveal-hero" :total-docs="totalDocs" :high-medium-ratio="highMediumRatio"
        :total-categories="totalCategories" />

      <!-- 2. 可视化图表网格排列 -->
      <div class="charts-dashboard-grid">
        <AnalysisCategoryPie class="analysis-motion reveal-pie" :data="categoryPieData" />

        <AnalysisStageBar class="analysis-motion reveal-bar" :data="stageBarData" />

        <AnalysisRiskRadar class="analysis-motion reveal-radar" :data="riskRadarData" />

        <AnalysisGauge class="analysis-motion reveal-gauge" :value="lowRiskPercent" />
      </div>
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

// 导入图表子组件
import AnalysisHero from '../components/analysis/AnalysisHero.vue'
import AnalysisCategoryPie from '../components/analysis/AnalysisCategoryPie.vue'
import AnalysisStageBar from '../components/analysis/AnalysisStageBar.vue'
import AnalysisRiskRadar from '../components/analysis/AnalysisRiskRadar.vue'
import AnalysisGauge from '../components/analysis/AnalysisGauge.vue'

const search = ref('')

// --- 数据计算逻辑 ---

// 文献总数
const totalDocs = computed(() => docs.length)

// 中高风险占比
const highMediumRatio = computed(() => {
  if (!docs.length) return 0
  const count = docs.filter(d => ['高', '中'].includes(d.riskLevel)).length
  return Math.round((count / docs.length) * 100)
})

// 去重合规类别总数
const totalCategories = computed(() => {
  return new Set(docs.map(d => d.category)).size
})

// 饼图数据 (分类及频次)
const categoryPieData = computed(() => {
  const map = {}
  docs.forEach(doc => {
    if (doc.category) {
      map[doc.category] = (map[doc.category] || 0) + 1
    }
  })
  return Object.entries(map).map(([name, value]) => ({ name, value }))
})

// 条形图数据 (业务环节及频次)
const stageBarData = computed(() => {
  const map = {}
  docs.forEach(doc => {
    if (doc.businessStage) {
      map[doc.businessStage] = (map[doc.businessStage] || 0) + 1
    }
  })
  return Object.entries(map).map(([name, value]) => ({ name, value }))
})

// 雷达图数据 (地域及多维风险数)
const riskRadarData = computed(() => {
  const map = {}
  docs.forEach(doc => {
    if (!doc.region) return
    if (!map[doc.region]) {
      map[doc.region] = { region: doc.region, high: 0, medium: 0, low: 0 }
    }
    if (doc.riskLevel === '高') map[doc.region].high++
    else if (doc.riskLevel === '中') map[doc.region].medium++
    else if (doc.riskLevel === '低') map[doc.region].low++
  })
  return Object.values(map)
})

// 仪表盘安全级低风险百分比
const lowRiskPercent = computed(() => {
  if (!docs.length) return 0
  const count = docs.filter(d => d.riskLevel === '低').length
  return Math.round((count / docs.length) * 100)
})

// --- 渐显入场动效控制 ---
const observedElements = new WeakSet()
let revealObserver

const setupAnalysisMotion = () => {
  if (typeof window === 'undefined') return
  const targets = document.querySelectorAll('.analysis-page .analysis-motion')
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
  setupAnalysisMotion()
})

onBeforeUnmount(() => {
  revealObserver?.disconnect()
})
</script>

<style scoped>
.analysis-page {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  color: var(--color-text, #ffffff);
}

/* 渐变星空网格背景 */
.analysis-page::before {
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

.analysis-shell {
  position: relative;
  z-index: 1;
  width: min(1440px, calc(100% - 48px));
  margin: 0 auto;
  padding: clamp(60px, 8vw, 100px) 0 92px;
}

/* 动效入场状态 */
.analysis-motion {
  opacity: 0;
  filter: blur(8px);
  transform: translate3d(0, 26px, 0) scale(0.99);
  transition:
    opacity 0.76s var(--ease-premium),
    filter 0.76s var(--ease-premium),
    transform 0.76s var(--ease-premium);
  will-change: opacity, filter, transform;
}

.analysis-motion.is-visible {
  opacity: 1;
  filter: blur(0);
  transform: translate3d(0, 0, 0) scale(1);
}

.reveal-hero {
  transition-delay: 50ms;
}

.reveal-pie {
  transition-delay: 150ms;
}

.reveal-bar {
  transition-delay: 200ms;
}

.reveal-radar {
  transition-delay: 250ms;
}

.reveal-gauge {
  transition-delay: 300ms;
}

.charts-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(20px, 2.6vw, 32px);
}

@media (min-width: 860px) {
  .charts-dashboard-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 700px) {
  .analysis-shell {
    width: min(1440px, calc(100% - 32px));
  }
}
</style>
