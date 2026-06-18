<template>
  <article class="document-card" :class="[`tone-${doc.tone}`, { 'is-expanded': expanded }]">
    <div class="card-main">
      <div class="document-body">
        <div class="document-meta">
          <span class="type-badge">{{ doc.displayType }}</span>
          <span class="date-line">
            <IconGlyph name="clock" />
            {{ doc.dateLabel }}
          </span>
          <span class="risk-pill" :class="`risk-${doc.riskLevel}`">{{ doc.riskLevel }}风险</span>
        </div>

        <h2>{{ doc.title }}</h2>

        <div class="tag-row">
          <span v-for="tag in doc.tags" :key="tag">#{{ tag }}</span>
        </div>

        <p class="summary">{{ doc.summary }}</p>
      </div>

      <aside class="keyword-area" aria-label="文献高频词">
        <div>
          <p>核心高频词</p>
          <strong>{{ doc.keywordPreview }}</strong>
        </div>

        <button type="button" @click="$emit('toggle-detail', doc.id)">
          {{ expanded ? '收起详情' : '查看详情' }}
          <IconGlyph name="external" />
        </button>
      </aside>
    </div>

    <div v-if="expanded" class="detail-panel">
      <div>
        <span>文本节选</span>
        <p>{{ doc.excerpt }}</p>
      </div>
      <div>
        <span>合规分析</span>
        <p>{{ doc.analysis }}</p>
      </div>
      <a :href="doc.sourceUrl" target="_blank" rel="noreferrer">
        {{ doc.sourceName }}
        <IconGlyph name="external" />
      </a>
    </div>
  </article>
</template>

<script setup>
import IconGlyph from './IconGlyph.vue'

defineProps({
  doc: {
    type: Object,
    required: true,
  },
  expanded: {
    type: Boolean,
    default: false,
  },
})

defineEmits(['toggle-detail'])
</script>

<style scoped>
.document-card {
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  background:
    radial-gradient(circle at 0% 0%, rgba(255, 255, 255, 0.03), transparent 34%),
    linear-gradient(145deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.01)), rgba(20, 20, 20, 0.75);
  box-shadow: var(--shadow-deep);
  backdrop-filter: blur(18px);
  transition:
    border-color 0.36s var(--ease-premium),
    transform 0.36s var(--ease-premium),
    box-shadow 0.36s var(--ease-premium);
}

.document-card.is-expanded {
  border-color: color-mix(in srgb, var(--tone-color, var(--color-gold)) 42%, rgba(255, 255, 255, 0.16));
  box-shadow: 0 42px 120px rgba(0, 0, 0, 0.5);
}

.document-card::before {
  position: absolute;
  inset: 0 auto 0 0;
  width: 3px;
  background: var(--tone-color, var(--color-gold));
  opacity: 0.72;
  transition:
    opacity 0.36s var(--ease-premium),
    transform 0.36s var(--ease-premium);
  content: '';
}

.document-card.is-expanded::before,
.document-card:hover::before {
  opacity: 1;
  transform: scaleY(1.02);
}

.document-card:hover {
  border-color: rgba(255, 255, 255, 0.24);
  box-shadow: 0 38px 110px rgba(0, 0, 0, 0.46);
  transform: translateY(-3px);
}

.card-main {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 220px;
  gap: 34px;
  padding: clamp(24px, 3.2vw, 36px);
}

.document-body {
  min-width: 0;
}

.document-meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.type-badge,
.risk-pill {
  display: inline-flex;
  align-items: center;
  font-size: 12px;
  font-weight: 900;
}

.type-badge {
  color: var(--tone-color, var(--color-gold));
}

.date-line {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: rgba(255, 255, 255, 0.64);
  font-size: 13px;
  font-weight: 850;
}

.date-line .icon-glyph {
  font-size: 15px;
}

.risk-高 {
  color: #f0a08d;
}

.risk-中 {
  color: #e2c581;
}

.risk-低 {
  color: #93d0bd;
}

h2 {
  max-width: 820px;
  margin: 0;
  color: var(--color-text);
  font-size: clamp(22px, 2.4vw, 30px);
  font-weight: 900;
  line-height: 1.28;
  transition: color 0.3s var(--ease-premium);
}

.document-card:hover h2 {
  color: #ffffff;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 18px 0;
}

.tag-row span {
  padding: 5px 9px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: rgba(255, 255, 255, 0.62);
  font-size: 12px;
  font-weight: 900;
  transition:
    background 0.3s var(--ease-premium),
    color 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}

.document-card:hover .tag-row span {
  background: rgba(255, 255, 255, 0.11);
  color: rgba(255, 255, 255, 0.78);
  transform: translateY(-1px);
}

.summary {
  display: -webkit-box;
  max-width: 850px;
  margin: 0;
  overflow: hidden;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  color: rgba(255, 255, 255, 0.68);
  font-size: 16px;
  line-height: 1.75;
}

.keyword-area {
  display: flex;
  align-items: flex-end;
  flex-direction: column;
  justify-content: space-between;
  gap: 26px;
  text-align: right;
}

.keyword-area p {
  margin: 0 0 8px;
  color: rgba(255, 255, 255, 0.38);
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.13em;
}

.keyword-area strong {
  display: block;
  color: rgba(255, 255, 255, 0.82);
  font-size: 15px;
  line-height: 1.55;
}

.keyword-area button {
  display: inline-flex;
  min-width: 156px;
  min-height: 50px;
  align-items: center;
  justify-content: center;
  gap: 10px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 999px;
  background: #ffffff;
  color: #090d16;
  cursor: pointer;
  font-size: 14px;
  font-weight: 950;
  transition:
    transform 0.3s var(--ease-premium),
    background 0.3s var(--ease-premium);
}

.keyword-area button:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
}

.keyword-area button:active {
  transform: translateY(0) scale(0.97);
}

.keyword-area button .icon-glyph {
  font-size: 17px;
  transition: transform 0.3s var(--ease-premium);
}

.keyword-area button:hover .icon-glyph {
  transform: translate(2px, -2px);
}

.detail-panel {
  display: grid;
  grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr);
  gap: 24px;
  padding: 0 clamp(24px, 3.2vw, 36px) clamp(24px, 3.2vw, 36px);
  transform-origin: top;
  animation: detail-in 0.44s var(--ease-premium) both;
}

.detail-panel > div {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 18px;
}

.detail-panel span {
  display: block;
  margin-bottom: 8px;
  color: var(--color-gold);
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.08em;
}

.detail-panel p {
  margin: 0;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  line-height: 1.75;
}

.detail-panel a {
  display: inline-flex;
  grid-column: 1 / -1;
  width: fit-content;
  align-items: center;
  gap: 8px;
  color: #cbd5e1;
  font-size: 13px;
  font-weight: 900;
  text-decoration: none;
}

.tone-policy {
  --tone-color: #c8a866;
}

.tone-news {
  --tone-color: #8cc9b5;
}

.tone-corporate {
  --tone-color: #d3a078;
}

.tone-global {
  --tone-color: #9fb7ff;
}

.tone-data {
  --tone-color: #bba2ff;
}

.tone-esg {
  --tone-color: #93d0bd;
}

@keyframes detail-in {
  from {
    opacity: 0;
    transform: translateY(-10px) scaleY(0.98);
  }

  to {
    opacity: 1;
    transform: translateY(0) scaleY(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .document-card,
  .document-card::before,
  .tag-row span,
  .keyword-area button,
  .keyword-area button .icon-glyph {
    transition: none;
  }

  .detail-panel {
    animation: none;
  }
}

@media (max-width: 860px) {
  .card-main {
    grid-template-columns: 1fr;
  }

  .keyword-area {
    align-items: flex-start;
    text-align: left;
  }

  .detail-panel {
    grid-template-columns: 1fr;
  }
}
</style>
