<template>
  <main class="about-page">
    <!-- 流式背景视频 -->
    <SubpageBgVideo
      src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260422_112520_ee819691-f2e8-4c54-bb77-3fb72c84eaa5.mp4" />

    <!-- 头部导航栏 -->
    <LibraryTopNav v-model:search="search" />

    <!-- 页面核心包围壳 -->
    <div class="about-shell">
      <!-- 1. 顶部项目背景说明 -->
      <AboutHero class="about-motion reveal-hero" />

      <!-- 2. 数据采集清洗标准 -->
      <AboutStandard class="about-motion reveal-standard" />

      <!-- 3. 合规分类体系卡片 -->
      <AboutDimensions class="about-motion reveal-dimensions" />

      <!-- 4. 技术选型与数据字典 -->
      <AboutStack class="about-motion reveal-stack" />
    </div>

    <!-- 页脚 -->
    <LibraryFooter />
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'

// 导入公共组件
import LibraryTopNav from '../components/gonggongzujian/LibraryTopNav.vue'
import SubpageBgVideo from '../components/gonggongzujian/SubpageBgVideo.vue'
import LibraryFooter from '../components/library/LibraryFooter.vue'

// 导入项目介绍页子组件
import AboutHero from '../components/about/AboutHero.vue'
import AboutStandard from '../components/about/AboutStandard.vue'
import AboutDimensions from '../components/about/AboutDimensions.vue'
import AboutStack from '../components/about/AboutStack.vue'

const search = ref('')

// --- 渐显入场动效控制 ---
const observedElements = new WeakSet()
let revealObserver

const setupAboutMotion = () => {
  if (typeof window === 'undefined') return
  const targets = document.querySelectorAll('.about-page .about-motion')
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
  setupAboutMotion()
})

onBeforeUnmount(() => {
  revealObserver?.disconnect()
})
</script>

<style scoped>
.about-page {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  color: var(--color-text, #ffffff);
}

/* 渐变星空网格背景 */
.about-page::before {
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

.about-shell {
  position: relative;
  z-index: 1;
  width: min(1440px, calc(100% - 48px));
  margin: 0 auto;
  padding: clamp(60px, 8vw, 100px) 0 92px;
}

/* 动效入场状态 */
.about-motion {
  opacity: 0;
  filter: blur(8px);
  transform: translate3d(0, 26px, 0) scale(0.99);
  transition:
    opacity 0.76s var(--ease-premium),
    filter 0.76s var(--ease-premium),
    transform 0.76s var(--ease-premium);
  will-change: opacity, filter, transform;
}

.about-motion.is-visible {
  opacity: 1;
  filter: blur(0);
  transform: translate3d(0, 0, 0) scale(1);
}

.reveal-hero {
  transition-delay: 50ms;
}

.reveal-standard {
  transition-delay: 150ms;
}

.reveal-dimensions {
  transition-delay: 200ms;
}

.reveal-stack {
  transition-delay: 250ms;
}

@media (max-width: 700px) {
  .about-shell {
    width: min(1440px, calc(100% - 32px));
  }
}
</style>
