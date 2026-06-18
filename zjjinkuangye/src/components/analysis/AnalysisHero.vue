<template>
  <header class="analysis-hero">
    <div class="hero-content">
      <span class="subtitle">COMPLIANCE INTELLIGENCE DASHBOARD</span>
      <h1>合规数据可视化驾驶舱</h1>
      <p class="description">
        通过图形化界面多维度分析跨境合规公开文献。图表从主题类别、风险等级、业务生命周期、地域分布等视角进行数据挖掘与联动透视。
      </p>
    </div>

    <div class="metrics-grid">
      <div class="metric-card">
        <p class="card-label">已清洗合规文献</p>
        <strong class="card-value">{{ totalDocs }} <span class="unit">篇</span></strong>
        <span class="card-desc">平台数据源总计记录数</span>
      </div>

      <div class="metric-card warning-metric">
        <p class="card-label">中高风险文献率</p>
        <strong class="card-value">{{ highMediumRatio }}<span class="unit">%</span></strong>
        <span class="card-desc">需要重点关注与应对建议的文献</span>
      </div>

      <div class="metric-card">
        <p class="card-label">政策主题大类</p>
        <strong class="card-value">{{ totalCategories }} <span class="unit">个</span></strong>
        <span class="card-desc">已涵盖的核心合规政策分支</span>
      </div>
    </div>
  </header>
</template>

<script setup>
defineProps({
  totalDocs: {
    type: Number,
    required: true,
  },
  highMediumRatio: {
    type: Number,
    required: true,
  },
  totalCategories: {
    type: Number,
    required: true,
  },
})
</script>

<style scoped>
.analysis-hero {
  margin-bottom: clamp(40px, 5vw, 60px);
}

.hero-content {
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
  background: linear-gradient(135deg, #ffffff 60%, rgba(255, 255, 255, 0.7));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
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

.warning-metric::before {
  background: #f0a08d;
}

.card-label {
  margin: 0 0 10px;
  font-size: 13px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.6);
}

.card-value {
  display: block;
  font-size: clamp(34px, 3.8vw, 44px);
  font-weight: 900;
  line-height: 1.1;
  color: #ffffff;
  margin-bottom: 8px;
}

.unit {
  font-size: 14px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.65);
  margin-left: 4px;
}

.card-desc {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
}
</style>
