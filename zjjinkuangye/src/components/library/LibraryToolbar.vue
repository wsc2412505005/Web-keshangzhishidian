<template>
  <section class="library-toolbar" aria-labelledby="library-title">
    <div>
      <h1 id="library-title">合规文献资料库</h1>
      <p>显示 {{ total }} 条合规文献中的 {{ filteredTotal }} 条 · 当前分类：{{ activeLabel }}</p>
    </div>

    <div class="toolbar-actions">
      <button type="button" @click="$emit('reset')">
        <IconGlyph name="filter" />
        重置筛选
      </button>
      <button type="button" @click="$emit('toggle-sort')">
        <IconGlyph name="sort" />
        {{ sortOrder === 'desc' ? '最新发布' : '最早发布' }}
      </button>
    </div>
  </section>
</template>

<script setup>
import IconGlyph from './IconGlyph.vue'

defineProps({
  total: {
    type: Number,
    required: true,
  },
  filteredTotal: {
    type: Number,
    required: true,
  },
  activeLabel: {
    type: String,
    required: true,
  },
  sortOrder: {
    type: String,
    required: true,
  },
})

defineEmits(['reset', 'toggle-sort'])
</script>

<style scoped>
.library-toolbar {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 28px;
  margin-bottom: 34px;
}

h1 {
  margin: 0;
  color: var(--color-text);
  font-size: clamp(34px, 4.6vw, 52px);
  font-weight: 900;
  line-height: 1.02;
}

p {
  margin: 10px 0 0;
  color: var(--color-muted);
  font-size: 17px;
  line-height: 1.6;
}

.toolbar-actions {
  display: flex;
  flex: 0 0 auto;
  align-items: center;
  gap: 10px;
  padding-top: 8px;
}

button {
  display: inline-flex;
  min-height: 46px;
  align-items: center;
  justify-content: center;
  gap: 9px;
  padding: 0 18px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.04);
  color: rgba(255, 255, 255, 0.88);
  cursor: pointer;
  font-size: 14px;
  font-weight: 850;
  transition:
    border-color 0.3s var(--ease-premium),
    background 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}

button:hover {
  border-color: rgba(255, 255, 255, 0.36);
  background: rgba(255, 255, 255, 0.08);
  transform: translateY(-1px);
}

button:active {
  transform: translateY(0) scale(0.975);
}

button .icon-glyph {
  font-size: 18px;
  transition: transform 0.3s var(--ease-premium);
}

button:hover .icon-glyph {
  transform: translateX(2px);
}

@media (max-width: 700px) {
  .library-toolbar {
    display: grid;
    gap: 18px;
  }

  .toolbar-actions {
    padding-top: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  button,
  button .icon-glyph {
    transition: none;
  }
}
</style>
