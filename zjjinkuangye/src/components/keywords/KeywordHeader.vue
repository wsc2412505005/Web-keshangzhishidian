<template>
  <header class="keyword-header">
    <div class="header-content">
      <span class="subtitle">KEYWORD STATISTICS</span>
      <h1>合规关键词特征分析</h1>
      <p class="description">
        平台通过对公开文本进行分词清洗与人工标注，提取出反映跨境合规动态的核心特征词。以下是关键词的多维度统计指标。
      </p>
    </div>

    <div class="metrics-grid">
      <div class="metric-card">
        <p class="card-label">唯一特征词总数</p>
        <strong class="card-value">{{ totalKeywords }}</strong>
        <span class="card-desc">已提取的去重高频词</span>
      </div>

      <div class="metric-card">
        <p class="card-label">平均文献标注量</p>
        <strong class="card-value">{{ avgKeywords }}</strong>
        <span class="card-desc">平均每篇文献特征词数</span>
      </div>

      <div class="metric-card top-keywords-card">
        <p class="card-label">最常出现特征词排行</p>
        <ul class="top-list">
          <li v-for="(item, index) in topKeywords" :key="item.name">
            <span class="rank-badge" :class="`rank-${index + 1}`">{{ index + 1 }}</span>
            <span class="keyword-name">{{ item.name }}</span>
            <span class="keyword-count">{{ item.count }} 次</span>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
defineProps({
  totalKeywords: {
    type: Number,
    required: true,
  },
  avgKeywords: {
    type: String,
    required: true,
  },
  topKeywords: {
    type: Array,
    required: true,
  },
})
</script>

<style scoped>
.keyword-header {
  margin-bottom: clamp(40px, 5vw, 60px);
}

.header-content {
  max-width: 800px;
  margin-bottom: clamp(30px, 4vw, 42px);
}

.subtitle {
  display: block;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.18em;
  color: var(--color-gold, #c8a866);
  margin-bottom: 12px;
  text-transform: uppercase;
}

h1 {
  font-size: clamp(28px, 3.2vw, 44px);
  font-weight: 900;
  line-height: 1.2;
  margin: 0 0 16px;
  color: var(--color-text, #ffffff);
}

.description {
  font-size: clamp(14px, 1.8vw, 17px);
  line-height: 1.7;
  color: var(--color-muted, #8e8e93);
  margin: 0;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: clamp(16px, 2vw, 24px);
}

.metric-card {
  position: relative;
  overflow: hidden;
  padding: 26px 30px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: radial-gradient(circle at 0% 0%, rgba(255, 255, 255, 0.02), transparent 40%),
              linear-gradient(145deg, rgba(255, 255, 255, 0.035), rgba(255, 255, 255, 0.005)),
              rgba(20, 20, 20, 0.62);
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-deep);
  transition: border-color 0.3s var(--ease-premium), transform 0.3s var(--ease-premium);
}

.metric-card:hover {
  border-color: rgba(255, 255, 255, 0.16);
  transform: translateY(-2px);
}

.metric-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 2px;
  height: 100%;
  background: var(--color-gold, #c8a866);
  opacity: 0.6;
}

.card-label {
  margin: 0 0 10px;
  font-size: 13px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.6);
}

.card-value {
  display: block;
  font-size: clamp(36px, 4vw, 48px);
  font-weight: 900;
  line-height: 1.1;
  color: var(--color-gold, #ffffff);
  margin-bottom: 8px;
}

.card-desc {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
}

.top-keywords-card {
  grid-column: span 1;
}

@media (min-width: 860px) {
  .metrics-grid {
    grid-template-columns: 1fr 1fr 1.5fr;
  }
}

.top-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.top-list li {
  display: flex;
  align-items: center;
  font-size: 14px;
}

.rank-badge {
  display: grid;
  place-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 900;
  margin-right: 12px;
  background: rgba(255, 255, 255, 0.08);
  color: rgba(255, 255, 255, 0.65);
}

.rank-1 {
  background: var(--color-gold, #c8a866);
  color: #000;
}

.rank-2 {
  background: rgba(200, 168, 102, 0.4);
  color: #fff;
}

.rank-3 {
  background: rgba(255, 255, 255, 0.16);
  color: #fff;
}

.keyword-name {
  color: rgba(255, 255, 255, 0.88);
  font-weight: 850;
  flex-grow: 1;
}

.keyword-count {
  color: var(--color-gold, #c8a866);
  font-weight: 900;
  font-size: 13px;
}
</style>
