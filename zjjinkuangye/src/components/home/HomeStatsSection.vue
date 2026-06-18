<template>
  <section class="stats-section">
    <!-- Heading Section with Divider -->
    <div class="section-heading">
      <span class="label">数据智能全景分析 | PANORAMIC DATA INTELLIGENCE</span>
      <h2>数据智能概览</h2>
      <div class="title-divider"></div>
      <p>基于已采集的公开文本资料，提取来源类型、合规主题、关键词与风险等级，形成课程项目的数据基础。</p>
    </div>
    <!-- Bento Grid Grid Layout matching shejitu/1.html -->
    <div class="stats-bento">
      <!-- Card 1: Total Managed Texts (Span 2) -->
      <article class="stat-card stat-card-large group">
        <div class="stat-content relative z-10">
          <span class="stat-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" class="svg-icon">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
          </span>
          <span class="meta-label">已整理文献总数 | TOTAL MANAGED TEXTS</span>
          <strong class="number-display">{{ metrics.total }}</strong>
          <p class="desc">汇集自三亚自贸港政策、跨国企业公开信息、国际行业规则与海外运营风险资料的合规文本语料库。</p>
        </div>
        <!-- Absolute Background Database Icon -->
        <div class="db-bg-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
            stroke-linejoin="round">
            <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
            <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
            <path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path>
          </svg>
        </div>
      </article>
      <!-- Card 2: Policy Documents -->
      <article class="stat-card group">
        <span class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
            stroke-linejoin="round" class="svg-icon">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
          </svg>
        </span>
        <span class="meta-label">政策法规文献 | POLICY DOCUMENTS</span>
        <strong class="number-display">{{ metrics.policies }}</strong>
        <div class="trend-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
            stroke-linejoin="round" class="trend-arrow">
            <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
            <polyline points="17 6 23 6 23 12"></polyline>
          </svg>
          <span>+12% 本月新增</span>
        </div>
      </article>
      <!-- Card 3: Industry News -->
      <article class="stat-card group">
        <span class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
            stroke-linejoin="round" class="svg-icon">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <path d="M16 8h2"></path>
            <path d="M16 12h2"></path>
            <path d="M16 16h2"></path>
            <path d="M6 8h6v8H6z"></path>
          </svg>
        </span>
        <span class="meta-label">行业与企业动态 | INDUSTRY NEWS</span>
        <strong class="number-display">{{ metrics.news }}</strong>
        <p class="sub-info">每日全球自动更新 | Daily updates</p>
      </article>
      <!-- Card 4: Corporate Announcements -->
      <article class="stat-card group">
        <span class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
            stroke-linejoin="round" class="svg-icon">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
        </span>
        <span class="meta-label">上市公司披露 | CORPORATE ANNOUNCEMENTS</span>
        <strong class="number-display">{{ metrics.company }}</strong>
        <p class="sub-info">上市公司合规披露 | Regulatory updates</p>
      </article>
      <!-- Card 5: Keywords (Span 2) -->
      <article class="stat-card stat-card-large stat-card-wide group">
        <div class="keyword-meta">
          <span class="meta-label">AI 提取合规关键词 | COMPLIANCE KEYWORDS</span>
          <strong class="number-display gold">{{ metrics.keywords }}</strong>
          <p class="desc">采用智能化自然语言处理技术抽取的跨境矿业合规核心词云。</p>
        </div>
        <div class="keyword-cloud">
          <span class="cloud-tag">ESG</span>
          <span class="cloud-tag">LEGAL</span>
          <span class="cloud-tag">RISK</span>
          <span class="cloud-tag">MINING</span>
          <span class="cloud-tag">COMPLIANCE</span>
          <span class="cloud-tag">CROSS-BORDER</span>
        </div>
      </article>
      <!-- Card 6: Risk Alerts -->
      <article class="stat-card stat-card-alert group">
        <span class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"
            stroke-linejoin="round" class="svg-icon">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
            <line x1="12" y1="9" x2="12" y2="13"></line>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
        </span>
        <span class="meta-label">合规风险预警 | RISK ALERTS</span>
        <strong class="number-display alert">{{ metrics.highRisk }}</strong>
        <div class="alert-pill">
          <span>需要立即关注 | IMMEDIATE ATTENTION</span>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
defineProps({
  metrics: {
    type: Object,
    required: true,
  },
})
</script>


<style scoped>
.stats-section {
  --risk-soft: #cbd5e1;
  --risk-soft-bg: rgba(203, 213, 225, 0.08);
  --risk-soft-line: rgba(203, 213, 225, 0.2);

  position: relative;
  overflow: hidden;
  padding: 118px clamp(20px, 5vw, 64px);
  background:
    radial-gradient(circle at 12% 12%, rgba(255, 255, 255, 0.04), transparent 28%),
    radial-gradient(circle at 86% 0%, rgba(255, 255, 255, 0.02), transparent 34%),
    linear-gradient(180deg, #000000 0%, #111111 54%, #000000 100%);
  color: var(--color-text);
}

.stats-section::before {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px);
  background-size: 72px 72px;
  mask-image: linear-gradient(180deg, transparent, #000 16%, #000 76%, transparent);
  content: "";
}

.section-heading {
  position: relative;
  max-width: 760px;
  margin: 0 auto 64px;
  text-align: center;
}

.section-heading .label {
  color: var(--color-gold);
  font-size: 13px;
  font-weight: 900;
  letter-spacing: 0.08em;
}

.section-heading h2 {
  margin: 12px 0 10px;
  font-family: var(--font-sans);
  font-size: clamp(32px, 4vw, 46px);
  font-weight: 850;
  line-height: 1.14;
  color: #fffaf0;
}

.title-divider {
  width: 96px;
  height: 3px;
  background: var(--color-gold);
  margin: 16px auto;
  border-radius: 999px;
}

.section-heading p {
  margin: 0;
  color: var(--color-muted);
  font-size: 17px;
  line-height: 1.8;
}

/* Bento Grid matching shejitu/1.html */
.stats-bento {
  position: relative;
  display: grid;
  max-width: 1240px;
  margin: 0 auto;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 24px;
}

.stat-card {
  position: relative;
  overflow: hidden;
  min-height: 240px;
  padding: clamp(24px, 3vw, 34px);
  border: 1px solid var(--color-line);
  border-radius: 16px;
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01)),
    rgba(20, 20, 20, 0.75);
  box-shadow: var(--shadow-deep);
  backdrop-filter: blur(18px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  transition:
    transform 0.45s var(--ease-premium),
    border-color 0.45s var(--ease-premium),
    box-shadow 0.45s var(--ease-premium),
    background 0.45s var(--ease-premium);
}

.stat-card:hover {
  transform: translateY(-6px);
  border-color: rgba(255, 255, 255, 0.25);
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.02)),
    rgba(30, 30, 30, 0.85);
  box-shadow: 0 42px 110px rgba(0, 0, 0, 0.48);
}

.stat-card-large {
  grid-column: span 2;
}

.stat-card-wide {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

/* SVG Icons style */
.stat-icon {
  display: inline-grid;
  width: 28px;
  height: 28px;
  margin-bottom: 24px;
  place-items: center;
  border: 0;
  border-radius: 0;
  background: transparent;
  box-shadow: none;
  color: rgba(255, 255, 255, 0.84);
  flex-shrink: 0;
  transition: transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.svg-icon {
  width: 24px;
  height: 24px;
}

.stat-card:hover .stat-icon {
  transform: scale(1.1) rotate(5deg);
}

.meta-label {
  display: block;
  color: rgba(255, 255, 255, 0.55);
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.number-display {
  display: block;
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: clamp(38px, 4.5vw, 56px);
  font-weight: 850;
  line-height: 1.1;
  margin: 8px 0 12px;
}

.desc {
  margin: 0;
  color: var(--color-muted);
  font-size: 14px;
  line-height: 1.6;
}

.sub-info {
  margin: auto 0 0;
  color: rgba(255, 255, 255, 0.45);
  font-size: 12px;
  font-weight: 800;
}

/* Card 1 Database Decoration */
.db-bg-icon {
  position: absolute;
  top: 18px;
  right: 18px;
  color: #ffffff;
  opacity: 0.06;
  width: 130px;
  height: 130px;
  pointer-events: none;
  transition: transform 0.8s var(--ease-premium), opacity 0.8s var(--ease-premium);
}

.stat-card-large:hover .db-bg-icon {
  transform: scale(1.06) rotate(-3deg);
  opacity: 0.1;
}

/* Card 2 Trend Badge */
.trend-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #ffffff;
  font-size: 11px;
  font-weight: 900;
  margin-top: auto;
}

.trend-arrow {
  width: 12px;
  height: 12px;
}

/* Card 5 Keywords layout */
.keyword-meta {
  flex: 1;
  min-width: 0;
}

.number-display.gold {
  color: var(--color-gold);
}

.keyword-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  max-width: 240px;
  flex-shrink: 0;
}

.cloud-tag {
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.03);
  color: rgba(255, 255, 255, 0.7);
  font-size: 10px;
  font-weight: 900;
  transition: all 0.3s var(--ease-premium);
}

.stat-card-wide:hover .cloud-tag {
  border-color: rgba(255, 255, 255, 0.2);
  color: var(--color-gold);
  background: rgba(255, 255, 255, 0.06);
}

.cloud-tag:hover {
  transform: scale(1.06);
  border-color: var(--color-gold) !important;
  background: var(--color-gold) !important;
  color: #000000 !important;
}

/* Card 6 Alert Layout */
.stat-card-alert {
  border-left: 4px solid var(--risk-soft);
}

.stat-card-alert .stat-icon {
  color: var(--risk-soft);
}

.number-display.alert {
  color: var(--risk-soft);
}

.alert-pill {
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  border-radius: 6px;
  background: var(--risk-soft-bg);
  border: 1px solid var(--risk-soft-line);
  color: #f1f5f9;
  font-size: 10px;
  font-weight: 900;
  letter-spacing: 0.05em;
  margin-top: auto;
  text-transform: uppercase;
}

@media (max-width: 980px) {
  .stats-bento {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .stats-section {
    padding: 72px 18px;
  }

  .stats-bento {
    grid-template-columns: 1fr;
  }

  .stat-card-large,
  .stat-card-wide {
    grid-column: span 1;
  }

  .stat-card-wide {
    flex-direction: column;
    align-items: flex-start;
  }

  .keyword-cloud {
    max-width: 100%;
    margin-top: 12px;
  }
}
</style>
