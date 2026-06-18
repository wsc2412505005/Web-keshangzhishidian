<template>
  <aside class="library-sidebar">
    <div class="sidebar-sticky">
      <section class="category-panel" aria-labelledby="category-title">
        <h2 id="category-title">文献分类</h2>

        <div class="category-list">
          <button
            v-for="category in categories"
            :key="category.key"
            class="category-button"
            :class="{ 'is-active': category.key === activeCategory }"
            type="button"
            @click="$emit('select-category', category.key)"
          >
            <span>{{ category.label }}</span>
            <small>{{ category.count }}</small>
            <IconGlyph name="chevron-right" />
          </button>
        </div>
      </section>

      <section class="insight-card">
        <div class="insight-copy">
          <h3>合规动态看板</h3>
          <p>
            {{ insight.total }} 条公开文本，覆盖 {{ insight.sourceTypes }} 类资料来源； 高风险样本
            {{ insight.highRisk }} 条。
          </p>
          <a href="#keyword-analysis">
            了解更多
            <IconGlyph name="arrow-right" />
          </a>
        </div>

        <div class="insight-visual" aria-hidden="true">
          <IconGlyph name="analytics" />
        </div>
      </section>
    </div>
  </aside>
</template>

<script setup>
import IconGlyph from './IconGlyph.vue'

defineProps({
  categories: {
    type: Array,
    required: true,
  },
  activeCategory: {
    type: String,
    required: true,
  },
  insight: {
    type: Object,
    required: true,
  },
})

defineEmits(['select-category'])
</script>

<style scoped>
.library-sidebar {
  width: 280px;
  flex: 0 0 280px;
  min-width: 0;
}

.sidebar-sticky {
  position: sticky;
  top: 104px;
  display: grid;
  gap: 42px;
}

h2 {
  margin: 0 0 22px;
  color: var(--color-text);
  font-size: 28px;
  line-height: 1.14;
}

.category-list {
  display: grid;
  gap: 8px;
}

.category-button {
  position: relative;
  display: grid;
  width: 100%;
  min-height: 48px;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 10px;
  padding: 0 14px 0 18px;
  overflow: hidden;
  border: 1px solid transparent;
  border-radius: 999px;
  background: transparent;
  color: rgba(255, 255, 255, 0.68);
  cursor: pointer;
  text-align: left;
  transition:
    color 0.3s var(--ease-premium),
    border-color 0.3s var(--ease-premium),
    background 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}

.category-button span {
  min-width: 0;
  font-size: 14px;
  font-weight: 850;
}

.category-button small {
  color: rgba(255, 255, 255, 0.42);
  font-size: 12px;
  font-weight: 900;
}

.category-button .icon-glyph {
  color: currentColor;
  font-size: 17px;
  opacity: 0;
  transform: translateX(-4px);
  transition:
    opacity 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}

.category-button:hover,
.category-button.is-active {
  border-color: rgba(255, 255, 255, 0.16);
  background: rgba(255, 255, 255, 0.08);
  color: var(--color-gold);
  transform: translateX(3px);
}

.category-button:active {
  transform: translateX(2px) scale(0.985);
}

.category-button:hover .icon-glyph,
.category-button.is-active .icon-glyph {
  opacity: 1;
  transform: translateX(0);
}

.insight-card {
  position: relative;
  overflow: hidden;
  min-height: 186px;
  padding: 26px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  background:
    radial-gradient(circle at 88% 100%, rgba(255, 255, 255, 0.06), transparent 36%),
    linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01)), rgba(20, 20, 20, 0.75);
  box-shadow: var(--shadow-deep);
  backdrop-filter: blur(18px);
}

.insight-copy {
  position: relative;
  z-index: 1;
}

.insight-card h3 {
  margin: 0 0 12px;
  color: rgba(255, 255, 255, 0.78);
  font-size: 15px;
}

.insight-card p {
  margin: 0 0 20px;
  color: rgba(255, 255, 255, 0.52);
  font-size: 13px;
  font-weight: 750;
  line-height: 1.7;
}

.insight-card a {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--color-gold);
  font-size: 13px;
  font-weight: 900;
  text-decoration: none;
}

.insight-visual {
  position: absolute;
  right: 10px;
  bottom: 10px;
  display: grid;
  width: 74px;
  height: 74px;
  place-items: center;
  border-radius: 8px;
  background: rgba(6, 8, 7, 0.26);
  color: rgba(255, 255, 255, 0.06);
  font-size: 58px;
}

@media (max-width: 980px) {
  .library-sidebar {
    width: 100%;
    flex-basis: auto;
    max-width: 100%;
  }

  .sidebar-sticky {
    position: static;
    min-width: 0;
  }

  .category-panel {
    min-width: 0;
    max-width: 100%;
  }

  .category-list {
    display: flex;
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    padding-bottom: 6px;
    scroll-snap-type: x proximity;
    scrollbar-width: none;
  }

  .category-list::-webkit-scrollbar {
    display: none;
  }

  .category-button {
    width: auto;
    min-width: max-content;
    scroll-snap-align: start;
  }

  .category-button:hover,
  .category-button.is-active {
    transform: translateY(-1px);
  }

  .category-button:active {
    transform: translateY(0) scale(0.985);
  }

  .insight-card {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .category-button,
  .category-button .icon-glyph {
    transition: none;
  }
}
</style>
