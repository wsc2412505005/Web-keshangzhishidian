<template>
  <section class="related-docs-section">
    <div class="section-header">
      <h2>关联文献材料 ({{ docs.length }} 篇)</h2>
      <p v-if="keyword">
        以下是包含特征词 <span class="highlight-kw">#{{ keyword }}</span> 的所有跨境政策与企业公告数据。
      </p>
    </div>

    <div v-if="!docs.length" class="empty-docs">
      <p>暂无关联文献。请在词云中点击选择特征词。</p>
    </div>

    <div v-else class="document-list">
      <div
        v-for="(doc, index) in docs"
        :key="doc.id"
        class="document-item"
        :style="{ '--reveal-delay': `${index * 80}ms` }"
      >
        <LibraryCard
          :doc="doc"
          :expanded="expandedId === doc.id"
          @toggle-detail="toggleDetail"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, watch } from 'vue'
import LibraryCard from '../library/LibraryCard.vue'

const props = defineProps({
  keyword: {
    type: String,
    default: '',
  },
  docs: {
    type: Array,
    required: true,
  },
})

const expandedId = ref(null)

// 当切换关键词时，收起已展开的卡片
watch(() => props.keyword, () => {
  expandedId.value = null
})

const toggleDetail = (id) => {
  expandedId.value = expandedId.value === id ? null : id
}
</script>

<style scoped>
.related-docs-section {
  display: flex;
  flex-direction: column;
  gap: clamp(16px, 2.4vw, 24px);
  margin-top: clamp(40px, 6vw, 60px);
}

.section-header h2 {
  font-size: clamp(20px, 2.4vw, 26px);
  font-weight: 900;
  margin: 0 0 8px;
  color: var(--color-text, #ffffff);
}

.section-header p {
  font-size: 13.5px;
  color: var(--color-muted, #8e8e93);
  margin: 0;
}

.highlight-kw {
  color: var(--color-gold, #c8a866);
  font-weight: 900;
}

.empty-docs {
  padding: 40px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  background: rgba(255, 255, 255, 0.01);
  text-align: center;
  color: var(--color-muted, #8e8e93);
  font-size: 14px;
}

.document-list {
  display: grid;
  gap: 24px;
}

.document-item {
  animation: card-slide-in 0.6s var(--ease-premium) both;
  animation-delay: var(--reveal-delay, 0ms);
}

@keyframes card-slide-in {
  from {
    opacity: 0;
    transform: translateY(18px) scale(0.99);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
</style>
