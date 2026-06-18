<template>
  <header class="about-hero">
    <div class="hero-content">
      <span class="subtitle">PROJECT OVERVIEW</span>
      <h1>关于本平台与学术背景</h1>
      <p class="description">
        随着海南自由贸易港建设的深入，三亚已成为承接跨国矿业公司国际运营总部的重要基地。本平台是以<strong>“三亚紫金矿业跨境业务”</strong>为核心模拟背景搭建的合规文本分析与采集展示系统。
      </p>
      <p class="sub-description">
        作为一个数据驱动的学术模拟项目，平台旨在探索如何将零散的政策法规、行业新闻、企业公告进行结构化清洗与合规标注，最终实现透明、高效的跨境运营合规看板。
      </p>
    </div>
  </header>
</template>

<script setup>
// No props needed for this static description component
</script>

<style scoped>
.about-hero {
  margin-bottom: clamp(40px, 6vw, 64px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  padding-bottom: clamp(30px, 4vw, 48px);
}

.hero-content {
  max-width: 900px;
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
  font-size: clamp(28px, 3.6vw, 48px);
  font-weight: 900;
  line-height: 1.2;
  margin: 0 0 20px;
  color: var(--color-text, #ffffff);
  background: linear-gradient(135deg, #ffffff 60%, rgba(255, 255, 255, 0.65));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.description {
  font-size: clamp(16px, 2.2vw, 20px);
  line-height: 1.65;
  color: rgba(255, 255, 255, 0.88);
  margin: 0 0 16px;
}

.description strong {
  color: var(--color-gold, #c8a866);
  font-weight: 900;
}

.sub-description {
  font-size: clamp(14px, 1.8vw, 16px);
  line-height: 1.7;
  color: var(--color-muted, #8e8e93);
  margin: 0;
}
</style>
