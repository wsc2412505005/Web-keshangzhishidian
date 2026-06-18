<template>
  <section class="cta-section">
    <div class="cta-panel">
      <h2>开始构建跨境合规文本资料库</h2>
      <p>继续完善资料库、详情页和文本分析页，就可以形成完整的课程项目展示成果。</p>
      <div>
        <RouterLink to="/library">进入资料库</RouterLink>
        <a href="#about">查看项目说明</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.cta-section {
  padding: 104px clamp(20px, 5vw, 64px);
  background:
    linear-gradient(180deg, #111111, #000000);
  color: var(--color-text);
}

.cta-panel {
  max-width: 1240px;
  margin: 0 auto;
  padding: clamp(42px, 7vw, 86px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  background:
    radial-gradient(circle at 82% 0%, rgba(255, 255, 255, 0.04), transparent 30%),
    radial-gradient(circle at 18% 100%, rgba(255, 255, 255, 0.02), transparent 34%),
    linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));
  text-align: center;
  box-shadow: var(--shadow-deep);
}

h2 {
  max-width: 760px;
  margin: 0 auto;
  font-size: clamp(32px, 4.5vw, 56px);
  line-height: 1.12;
}

p {
  max-width: 620px;
  margin: 18px auto 36px;
  color: var(--color-muted);
  font-size: 18px;
  line-height: 1.8;
}

.cta-panel div {
  display: flex;
  justify-content: center;
  gap: 16px;
}

a {
  display: inline-flex;
  align-items: center;
  min-height: 52px;
  padding: 0 28px;
  border-radius: 999px;
  font-weight: 900;
  text-decoration: none;
  transition:
    transform 0.28s var(--ease-premium),
    background 0.28s var(--ease-premium),
    border-color 0.28s var(--ease-premium);
}

a:first-child {
  background: #f5efe2;
  color: #101812;
  box-shadow: 0 18px 38px rgba(0, 0, 0, 0.28);
}

a:last-child {
  border: 1px solid rgba(245, 239, 226, 0.18);
  color: #f5efe2;
}

a:hover {
  transform: translateY(-2px);
}

a:last-child:hover {
  border-color: rgba(200, 168, 102, 0.62);
  background: rgba(200, 168, 102, 0.12);
}

@media (max-width: 640px) {
  .cta-panel div {
    display: grid;
  }

  a {
    justify-content: center;
  }
}
</style>
