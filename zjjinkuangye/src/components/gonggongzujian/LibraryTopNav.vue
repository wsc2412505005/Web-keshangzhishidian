<template>
  <header :class="['library-topnav', { 'is-home': isHome }]">
    <div class="topnav-inner">
      <RouterLink class="brand" to="/">三亚紫金矿业文本分析与采集平台</RouterLink>

      <nav class="main-nav" aria-label="导航菜单">
        <RouterLink to="/">首页</RouterLink>
        <RouterLink to="/library">文本库</RouterLink>
        <RouterLink to="/keywords">关键词分析</RouterLink>
        <RouterLink to="/analysis">数据可视化</RouterLink>
        <RouterLink to="/about">项目介绍</RouterLink>
      </nav>

      <div class="utility-zone">
        <label class="search-box">
          <span class="sr-only">搜索合规文本</span>
          <input v-model="displaySearch" type="search" placeholder="搜索合规文本..." @keydown.enter="handleSearchSubmit" />
          <IconGlyph name="search" style="cursor: pointer;" @click="handleSearchSubmit" />
        </label>

        <button class="icon-button" type="button" aria-label="个人中心">
          <IconGlyph name="user" />
        </button>
        <button class="icon-button" type="button" aria-label="设置">
          <IconGlyph name="settings" />
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import IconGlyph from '../library/IconGlyph.vue'

const props = defineProps({
  search: {
    type: String,
    default: '',
  },
})

const emit = defineEmits(['update:search'])

const route = useRoute()
const router = useRouter()

// 首页搜索框使用本地状态，提交时再跳转到资料库
const localSearch = ref(props.search)

watch(() => props.search, (newVal) => {
  localSearch.value = newVal
})

const isHome = computed(() => route.path === '/')

// 资料库页同步父级搜索词，首页则暂存输入内容
const displaySearch = computed({
  get() {
    return route.path === '/library' ? props.search : localSearch.value
  },
  set(val) {
    localSearch.value = val
    if (route.path === '/library') {
      emit('update:search', val)
    }
  }
})

// 首页提交搜索时跳转到资料库并携带 search 查询参数
const handleSearchSubmit = () => {
  if (route.path !== '/library') {
    router.push({
      path: '/library',
      query: { search: localSearch.value }
    })
  }
}
</script>

<style scoped>
.library-topnav {
  position: sticky;
  top: 0;
  z-index: 10;
  border-bottom: 1px solid rgba(245, 239, 226, 0.1);
  background: rgba(6, 8, 7, 0.82);
  backdrop-filter: blur(22px);
  transition: background 0.3s var(--ease-premium), border-color 0.3s var(--ease-premium), backdrop-filter 0.3s var(--ease-premium);
}
.library-topnav.is-home {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  background: transparent;
  border-bottom: none;
  backdrop-filter: none;
}
.topnav-inner {
  display: flex;
  width: min(1440px, calc(100% - 48px));
  min-height: 72px;
  margin: 0 auto;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
}
.brand {
  flex: 0 0 auto;
  color: var(--color-text);
  font-size: clamp(18px, 2vw, 24px);
  font-weight: 900;
  text-decoration: none;
  white-space: nowrap;
}
.main-nav {
  display: flex;
  align-items: center;
  margin-left: auto;
  margin-right: clamp(34px, 5vw, 68px);
  /* Spacing from the search bar exactly like the reference image */
  gap: clamp(28px, 2.6vw, 44px);
}
.main-nav a {
  position: relative;
  padding: 26px 0 22px;
  color: rgba(245, 239, 226, 0.68);
  font-size: 14px;
  font-weight: 850;
  text-decoration: none;
  transition: color 0.32s var(--ease-premium);
}
.main-nav a::after {
  position: absolute;
  right: 0;
  bottom: 17px;
  left: 0;
  height: 2px;
  background: var(--color-gold);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.32s var(--ease-premium);
  content: "";
}
.main-nav a:hover,
.main-nav a.router-link-active {
  color: var(--color-gold);
}
.main-nav a:hover::after,
.main-nav a.router-link-active::after {
  transform: scaleX(1);
}
.utility-zone {
  display: flex;
  flex: 0 0 auto;
  align-items: center;
  gap: 10px;
}
.search-box {
  position: relative;
  display: flex;
  align-items: center;
}
.search-box input {
  width: min(300px, 24vw);
  height: 44px;
  border: 1px solid rgba(245, 239, 226, 0.09);
  border-radius: 999px;
  outline: none;
  background: rgba(245, 239, 226, 0.06);
  color: var(--color-text);
  font-size: 14px;
  font-weight: 700;
  padding: 0 46px 0 20px;
  transition:
    border-color 0.3s var(--ease-premium),
    background 0.3s var(--ease-premium);
}
.search-box input::placeholder {
  color: rgba(245, 239, 226, 0.48);
}
.search-box input:focus {
  border-color: rgba(200, 168, 102, 0.62);
  background: rgba(245, 239, 226, 0.09);
}
.search-box .icon-glyph {
  position: absolute;
  right: 17px;
  color: rgba(245, 239, 226, 0.72);
  font-size: 18px;
}
.icon-button {
  display: grid;
  width: 40px;
  height: 40px;
  place-items: center;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--color-gold);
  cursor: pointer;
  font-size: 20px;
  transition:
    background 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}
.icon-button:hover {
  background: rgba(200, 168, 102, 0.12);
  transform: translateY(-1px);
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
@media (max-width: 1060px) {
  .main-nav {
    display: none;
  }
  .search-box input {
    width: 260px;
  }
}
@media (max-width: 700px) {
  .topnav-inner {
    width: min(1440px, calc(100% - 32px));
    min-height: 68px;
  }
  .search-box {
    display: none;
  }
  .brand {
    font-size: 17px;
  }
}
</style>
