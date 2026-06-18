<template>
  <section class="keyword-cloud-section">
    <div class="section-header">
      <h2>特征词云图</h2>
      <p>点击下方任意特征词以查看其合规风险分布与关联文献列表。</p>
    </div>

    <div class="cloud-card">
      <div class="tags-wrapper">
        <button
          v-for="kw in sortedKeywords"
          :key="kw.name"
          type="button"
          class="cloud-tag"
          :class="[
            `weight-${getWeightClass(kw.count)}`,
            { 'is-active': activeKeyword === kw.name }
          ]"
          @click="$emit('select-keyword', kw.name)"
        >
          {{ kw.name }}
          <span class="tag-count">{{ kw.count }}</span>
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  keywords: {
    type: Array,
    required: true,
  },
  activeKeyword: {
    type: String,
    default: '',
  },
})

defineEmits(['select-keyword'])

const sortedKeywords = computed(() => {
  // 按照 count 从大到小排列，使词云整体看起来有节奏感，或者可以按名称字母随机排列，但为了可读性，先保留全部并排序
  return [...props.keywords].sort((a, b) => b.count - a.count)
})

// 根据出现频次定义权重等级
const getWeightClass = (count) => {
  if (count >= 5) return 'high-max'
  if (count === 4) return 'high'
  if (count === 3) return 'medium-high'
  if (count === 2) return 'medium'
  return 'low'
}
</script>

<style scoped>
.keyword-cloud-section {
  display: flex;
  flex-direction: column;
  gap: clamp(16px, 2.4vw, 24px);
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

.cloud-card {
  padding: clamp(24px, 3.6vw, 40px);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.015), transparent 60%),
              linear-gradient(145deg, rgba(255, 255, 255, 0.03), rgba(255, 255, 255, 0.005)),
              rgba(16, 16, 16, 0.55);
  backdrop-filter: blur(20px);
  box-shadow: var(--shadow-deep);
  min-height: 240px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tags-wrapper {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: clamp(10px, 1.6vw, 16px);
  max-width: 960px;
}

.cloud-tag {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.02);
  border-radius: 999px;
  color: rgba(255, 255, 255, 0.72);
  cursor: pointer;
  padding: 8px 16px;
  font-family: inherit;
  transition:
    transform 0.3s var(--ease-premium),
    background-color 0.3s var(--ease-premium),
    border-color 0.3s var(--ease-premium),
    box-shadow 0.3s var(--ease-premium),
    color 0.3s var(--ease-premium);
  will-change: transform, box-shadow;
}

/* 根据频次权重设置不同的字号、色调与间距 */
.weight-high-max {
  font-size: 19px;
  font-weight: 900;
  color: var(--color-gold, #c8a866);
  border-color: rgba(200, 168, 102, 0.24);
  background: rgba(200, 168, 102, 0.05);
  padding: 11px 22px;
}

.weight-high {
  font-size: 17px;
  font-weight: 850;
  color: #ebd5a3;
  border-color: rgba(200, 168, 102, 0.16);
  background: rgba(200, 168, 102, 0.02);
  padding: 10px 19px;
}

.weight-medium-high {
  font-size: 15px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.9);
  padding: 9px 17px;
}

.weight-medium {
  font-size: 13.5px;
  font-weight: 750;
  color: rgba(255, 255, 255, 0.7);
  padding: 8px 15px;
}

.weight-low {
  font-size: 12.5px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.5);
  padding: 7px 13px;
}

.tag-count {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 18px;
  height: 18px;
  padding: 0 4px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  font-size: 10px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.46);
  transition: background-color 0.3s, color 0.3s;
}

.cloud-tag:hover {
  transform: translateY(-2px) scale(1.03);
  border-color: rgba(255, 255, 255, 0.28);
  background: rgba(255, 255, 255, 0.06);
  color: #ffffff;
  box-shadow: 0 12px 34px rgba(0, 0, 0, 0.36);
}

.cloud-tag:hover .tag-count {
  background: rgba(255, 255, 255, 0.15);
  color: rgba(255, 255, 255, 0.88);
}

/* 悬浮到高频标签上产生微光发热动效 */
.weight-high-max:hover,
.weight-high:hover {
  border-color: rgba(200, 168, 102, 0.55);
  background: rgba(200, 168, 102, 0.08);
  box-shadow: 0 14px 40px rgba(200, 168, 102, 0.18);
}

/* 激活状态 */
.cloud-tag.is-active {
  background: #ffffff;
  border-color: #ffffff;
  color: #090d16;
  font-weight: 950;
  transform: translateY(-1px) scale(1.02);
  box-shadow: 0 18px 48px rgba(255, 255, 255, 0.15);
}

.cloud-tag.is-active .tag-count {
  background: rgba(9, 13, 22, 0.12);
  color: rgba(9, 13, 22, 0.65);
}
</style>
