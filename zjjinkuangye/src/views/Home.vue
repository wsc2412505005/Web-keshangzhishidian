<template>
  <main>
    <section class="home-page">
      <HeroVideoSwiper :slides="videoSlides" />
      <LibraryTopNav />
      <HeroCenter />
    </section>

    <HomeStatsSection id="library" :metrics="metrics" />
    <HomeVisualSection id="analysis" />
    <HomeCtaSection />
    <HomeFooter id="about" />
  </main>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted } from 'vue'
import docs from '../data/complianceDocs.json'
import HeroCenter from '../components/home/HeroCenter.vue'
import HeroVideoSwiper from '../components/home/HeroVideoSwiper.vue'
import HomeCtaSection from '../components/home/HomeCtaSection.vue'
import HomeFooter from '../components/home/HomeFooter.vue'
import LibraryTopNav from '../components/gonggongzujian/LibraryTopNav.vue'
import HomeStatsSection from '../components/home/HomeStatsSection.vue'
import HomeVisualSection from '../components/home/HomeVisualSection.vue'

// 轮播视频数据源：定义首页顶部 Hero 区域的背景视频及对应的主题文案
const videoSlides = [
  {
    src: '/1pc.mp4',
    label: '跨境矿业政策文本',
  },
  {
    src: '/2pc.mp4',
    label: '海南自贸港合规场景',
  },
  {
    src: '/3pc.mp4',
    label: '全球运营风险分析',
  },
]

// 核心统计指标：基于 complianceDocs.json 合规数据源，动态计算得出关键维度的数量
const metrics = computed(() => {
  // 提取去重后的来源类型和关键字列表
  const sourceTypes = new Set(docs.map((item) => item.sourceType))
  const keywords = new Set(docs.flatMap((item) => item.keywords))
  
  // 按不同类型及风险等级分类统计文档数量
  const policyCount = docs.filter(
    (item) => item.sourceType.includes('政策') || item.sourceType === '法律法规',
  ).length
  const newsCount = docs.filter((item) => item.sourceType.includes('新闻')).length
  const companyCount = docs.filter((item) => ['企业报告', '企业新闻'].includes(item.sourceType)).length
  const highRiskCount = docs.filter((item) => item.riskLevel === '高').length

  return {
    total: docs.length,            // 总文档数
    sourceTypes: sourceTypes.size, // 来源维度总数
    policies: policyCount,         // 政策法规数量
    news: newsCount,               // 新闻资讯数量
    company: companyCount,         // 企业层面的合规文件数
    keywords: keywords.size,       // 提取出的特征关键词总数
    highRisk: highRiskCount,       // 高风险指标警示数
  }
})

// 全局唯一的滚动进入检测观察器实例 (IntersectionObserver)
let revealObserver

// 首页滚动渐显动效配置：按不同的页面模块和 CSS 选择器，定义对应的入场动画样式和错峰延迟步长
const revealGroups = [
  {
    // 首屏文字与操作按钮：采用柔和渐显，中等延迟
    selector: '.hero-title-group h1, .hero-title-group p, .hero-actions',
    variant: 'motion-reveal-soft',
    step: 120,
  },
  {
    // 数据统计看板及指标卡片：采用卡片式的阶梯入场
    selector: '.stats-section .section-heading, .stats-section .stat-card',
    variant: 'motion-reveal-card',
    step: 90,
  },
  {
    // 特征展示区左侧文案与列表项：从左侧划入
    selector:
      '.visual-section .section-label, .visual-section h2, .visual-section .visual-copy > p, .visual-section .feature-item, .visual-section .action-btn-group',
    variant: 'motion-reveal-left',
    step: 85,
  },
  {
    // 特征展示区右侧图片/卡片面板：从右侧划入，整体淡入（不需要列表错峰）
    selector: '.visual-section .visual-frame',
    variant: 'motion-reveal-right',
    step: 0,
  },
  {
    // 底部呼吁行动区 (CTA)：柔和淡入
    selector: '.cta-section .cta-panel',
    variant: 'motion-reveal-soft',
    step: 90,
  },
]

// 核心动效初始化函数：为各区块内的目标元素挂载滚动入场动画，并兼容处理无动画或老旧浏览器
const setupHomeMotion = () => {
  if (typeof window === 'undefined') return

  // 检测系统是否开启了“减少动画”的无障碍设置，若开启则跳过过渡动画，直接显示
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  const canObserve = 'IntersectionObserver' in window
  const prepared = new Set() // 避免因选择器重复重叠导致元素被重复绑定

  revealGroups.forEach(({ selector, variant, step }) => {
    document.querySelectorAll(selector).forEach((element, index) => {
      if (!(element instanceof HTMLElement) || prepared.has(element)) return

      prepared.add(element)
      // 添加基类以及具体的动画变体样式类型
      element.classList.add('motion-reveal', variant)
      // 计算并设置 CSS 自定义变量，实现同一区块内子元素按次序“错峰/阶梯”渐显
      element.style.setProperty('--reveal-delay', `${Math.min(index * step, 520)}ms`)

      // 若系统开启了减弱动画或浏览器不支持 IntersectionObserver，则直接展示所有元素
      if (reduceMotion || !canObserve) {
        element.classList.add('is-visible')
      } else {
        // 否则将元素添加进观察名单中
        revealObserver?.observe(element)
      }
    })
  })
}

onMounted(async () => {
  // 等待 Vue 完成 DOM 更新，确保获取到最新渲染的 DOM 元素
  await nextTick()

  // 实例化交叉监听器，用于检测目标元素是否滚动进入或离开视口
  revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        // 当元素进入视口（或满足 rootMargin 范围）时，动态添加/移除 'is-visible' 类名以触发 CSS 动画
        entry.target.classList.toggle('is-visible', entry.isIntersecting)
      })
    },
    {
      threshold: 0.08, // 当元素有 8% 进入视口时便触发动画，提升响应敏捷度
      rootMargin: '120px 0px 120px 0px', // 上下边界向外扩展 120px，在元素尚未完全进屏时提前加载，使体验更丝滑
    },
  )

  // 挂载各区域滚动进入动画
  setupHomeMotion()
})

onBeforeUnmount(() => {
  // 组件销毁前主动断开观察，防范潜在的内存泄漏风险
  revealObserver?.disconnect()
})
</script>

<style scoped>
.home-page {
  position: relative;
  width: 100%;
  height: 100vh;
  min-height: 640px;
  overflow: hidden;
  background: #000000;
  color: #fff;
}

.home-page::after {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background:
    radial-gradient(circle at 50% 42%, rgba(255, 255, 255, 0.05), transparent 24%),
    radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.03), transparent 34%),
    linear-gradient(180deg, rgba(0, 0, 0, 0.68), rgba(0, 0, 0, 0.3) 42%, rgba(0, 0, 0, 0.86)),
    linear-gradient(90deg, rgba(0, 0, 0, 0.62), transparent 30%, transparent 70%, rgba(0, 0, 0, 0.58));
  content: "";
}

@media (max-width: 768px) {
  .home-page {
    min-height: 620px;
  }
}
</style>
