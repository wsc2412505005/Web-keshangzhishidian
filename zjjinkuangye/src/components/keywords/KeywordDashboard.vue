<template>
  <section class="keyword-dashboard">
    <div v-if="!keyword" class="no-selection">
      <div class="hint-box">
        <div class="pulsing-circle"></div>
        <h3>待选择关键词</h3>
        <p>请点击上方的词云标签，查看其与业务环节、风险等级及合规类别的关联透视数据。</p>
      </div>
    </div>

    <div v-else class="dashboard-grid">
      <!-- 关联概览卡片 -->
      <div class="card overview-card">
        <span class="card-subtitle">METRIC INSIGHTS</span>
        <h3>当前选择: <span class="highlight-word">{{ keyword }}</span></h3>
        <div class="overview-stats">
          <div class="stat-item">
            <strong>{{ docCount }}</strong>
            <span>关联文献总数</span>
          </div>
          <div class="stat-item">
            <strong>{{ riskRatio }}%</strong>
            <span>中高风险占比</span>
          </div>
        </div>
      </div>

      <!-- 风险等级分布卡 -->
      <div class="card risk-card">
        <h4>风险等级透视</h4>
        <div class="progress-list">
          <div v-for="level in levelConfig" :key="level.name" class="progress-item">
            <div class="progress-labels">
              <span class="level-name" :class="`risk-color-${level.key}`">{{ level.name }}风险</span>
              <span class="level-count">{{ level.count }} 篇 ({{ level.percent }}%)</span>
            </div>
            <div class="progress-bar-bg">
              <div
                class="progress-bar-fill"
                :class="`fill-${level.key}`"
                :style="{ width: `${level.percent}%` }"
              ></div>
            </div>
          </div>
        </div>
      </div>

      <!-- 业务环节分布 -->
      <div class="card stages-card">
        <h4>关联业务环节</h4>
        <ul class="meta-list">
          <li v-for="stage in businessStages" :key="stage.name">
            <span class="meta-name">{{ stage.name }}</span>
            <div class="bar-represent">
              <div class="bar-fill" :style="{ width: `${(stage.count / docCount) * 100}%` }"></div>
            </div>
            <span class="meta-count">{{ stage.count }} 次</span>
          </li>
        </ul>
      </div>

      <!-- 合规类别分布 -->
      <div class="card categories-card">
        <h4>关联政策主题</h4>
        <ul class="meta-list">
          <li v-for="cat in categories" :key="cat.name">
            <span class="meta-name">{{ cat.name }}</span>
            <div class="bar-represent">
              <div class="bar-fill theme-bar" :style="{ width: `${(cat.count / docCount) * 100}%` }"></div>
            </div>
            <span class="meta-count">{{ cat.count }} 次</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  keyword: {
    type: String,
    default: '',
  },
  docCount: {
    type: Number,
    default: 0,
  },
  riskLevels: {
    type: Object,
    default: () => ({ 高: 0, 中: 0, 低: 0 }),
  },
  businessStages: {
    type: Array,
    default: () => [],
  },
  categories: {
    type: Array,
    default: () => [],
  },
})

const riskRatio = computed(() => {
  if (!props.docCount) return 0
  const highMedium = (props.riskLevels['高'] || 0) + (props.riskLevels['中'] || 0)
  return Math.round((highMedium / props.docCount) * 100)
})

const levelConfig = computed(() => {
  const getPercent = (count) => (props.docCount ? Math.round((count / props.docCount) * 100) : 0)
  return [
    { key: 'high', name: '高', count: props.riskLevels['高'] || 0, percent: getPercent(props.riskLevels['高'] || 0) },
    { key: 'medium', name: '中', count: props.riskLevels['中'] || 0, percent: getPercent(props.riskLevels['中'] || 0) },
    { key: 'low', name: '低', count: props.riskLevels['低'] || 0, percent: getPercent(props.riskLevels['低'] || 0) },
  ]
})
</script>

<style scoped>
.keyword-dashboard {
  margin-top: clamp(24px, 4vw, 36px);
}

.no-selection {
  display: grid;
  place-content: center;
  min-height: 200px;
  padding: 40px;
  border-radius: 8px;
  border: 1px dashed rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.01);
  text-align: center;
}

.hint-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.pulsing-circle {
  width: 12px;
  height: 12px;
  background: var(--color-gold, #c8a866);
  border-radius: 50%;
  animation: pulse-ring 2s infinite ease-in-out;
}

@keyframes pulse-ring {
  0% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(200, 168, 102, 0.7);
  }
  70% {
    transform: scale(1.1);
    box-shadow: 0 0 0 8px rgba(200, 168, 102, 0);
  }
  100% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(200, 168, 102, 0);
  }
}

.no-selection h3 {
  font-size: 16px;
  font-weight: 900;
  margin: 0;
  color: rgba(255, 255, 255, 0.82);
}

.no-selection p {
  font-size: 13px;
  color: var(--color-muted, #8e8e93);
  margin: 0;
  max-width: 420px;
  line-height: 1.6;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: clamp(16px, 2.4vw, 24px);
}

.card {
  padding: clamp(20px, 3vw, 28px);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.07);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.025), rgba(255, 255, 255, 0.005)),
              rgba(16, 16, 16, 0.48);
  backdrop-filter: blur(14px);
  box-shadow: var(--shadow-deep);
}

h4 {
  font-size: 15px;
  font-weight: 900;
  margin: 0 0 18px;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 0.05em;
}

/* 概览卡片 */
.overview-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-subtitle {
  font-size: 11px;
  font-weight: 950;
  color: var(--color-gold, #c8a866);
  letter-spacing: 0.12em;
}

.overview-card h3 {
  font-size: 20px;
  font-weight: 900;
  margin: 12px 0 20px;
  color: #fff;
}

.highlight-word {
  color: var(--color-gold, #c8a866);
  border-bottom: 2px solid rgba(200, 168, 102, 0.36);
  padding-bottom: 2px;
}

.overview-stats {
  display: flex;
  gap: 28px;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-item strong {
  font-size: 32px;
  font-weight: 900;
  color: #ffffff;
  line-height: 1.1;
}

.stat-item span {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.42);
  margin-top: 4px;
}

/* 进度条样式 */
.progress-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.progress-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.progress-labels {
  display: flex;
  justify-content: space-between;
  font-size: 12.5px;
  font-weight: 850;
}

.level-name {
  font-weight: 900;
}

.risk-color-high { color: #f0a08d; }
.risk-color-medium { color: #e2c581; }
.risk-color-low { color: #93d0bd; }

.level-count {
  color: rgba(255, 255, 255, 0.5);
}

.progress-bar-bg {
  width: 100%;
  height: 6px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.05);
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  border-radius: 99px;
  transition: width 0.8s var(--ease-premium);
}

.fill-high { background: #f0a08d; }
.fill-medium { background: #e2c581; }
.fill-low { background: #93d0bd; }

/* 关联列表 */
.meta-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.meta-list li {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
}

.meta-name {
  width: 76px;
  color: rgba(255, 255, 255, 0.72);
  font-weight: 850;
  white-space: nowrap;
}

.bar-represent {
  flex-grow: 1;
  height: 4px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.04);
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.32);
  transition: width 0.6s var(--ease-premium);
}

.theme-bar {
  background: rgba(200, 168, 102, 0.46);
}

.meta-count {
  width: 32px;
  text-align: right;
  font-weight: 900;
  color: var(--color-gold, #c8a866);
}
</style>
