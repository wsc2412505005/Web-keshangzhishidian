<template>
  <section class="hero-center" aria-labelledby="home-title">
    <div class="hero-title-group">
      <h1 id="home-title">
        <span>紫金矿业跨境合规文本采集</span>
        <span>与前端展示平台</span>
      </h1>
      <p>
        面向海南自贸港与全球矿业运营场景，汇集公开政策、企业公告、国际规则与风险案例。
      </p>
      <div class="hero-actions">
        <RouterLink class="primary-action" to="/library">开始探索</RouterLink>
        <a class="secondary-action" href="#analysis">查看分析</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-center {
  position: relative;
  z-index: 4;
  display: grid;
  width: 100%;
  height: 100%;
  place-items: center;
  padding: 120px 28px 72px;
  text-align: center;
}

.hero-title-group {
  width: min(1120px, 100%);
}

h1 {
  margin: 0;
  color: #fffaf0;
  font-size: clamp(44px, 5.4vw, 76px);
  font-weight: 850;
  line-height: 1.04;
  text-shadow: 0 24px 80px rgba(0, 0, 0, 0.58);
}

h1 span {
  display: block;
  white-space: nowrap;
}

p {
  max-width: 760px;
  margin: 24px auto 0;
  color: rgba(245, 239, 226, 0.78);
  font-size: clamp(15px, 1.5vw, 18px);
  line-height: 1.85;
  text-shadow: 0 12px 38px rgba(0, 0, 0, 0.55);
}

.hero-actions {
  display: flex;
  justify-content: center;
  gap: 14px;
  margin-top: 36px;
}

.primary-action,
.secondary-action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 136px;
  min-height: 46px;
  padding: 0 24px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 900;
  text-decoration: none;
  transition:
    transform 0.28s var(--ease-premium),
    background 0.28s var(--ease-premium),
    border-color 0.28s var(--ease-premium),
    box-shadow 0.28s var(--ease-premium);
}

.primary-action {
  background: #f5efe2;
  color: #101812;
  box-shadow:
    0 18px 42px rgba(0, 0, 0, 0.28),
    inset 0 -8px 18px rgba(200, 168, 102, 0.22);
}

.secondary-action {
  border: 1px solid rgba(245, 239, 226, 0.36);
  color: #f5efe2;
  background: rgba(15, 24, 20, 0.36);
  backdrop-filter: blur(14px);
}

.primary-action:hover,
.secondary-action:hover {
  transform: translateY(-2px);
}

.primary-action:hover {
  box-shadow:
    0 22px 52px rgba(0, 0, 0, 0.34),
    inset 0 -8px 18px rgba(200, 168, 102, 0.28);
}

.secondary-action:hover {
  border-color: rgba(200, 168, 102, 0.84);
  background: rgba(200, 168, 102, 0.14);
}

@media (max-width: 720px) {
  h1 {
    font-size: clamp(36px, 12vw, 64px);
  }

  h1 span {
    white-space: normal;
  }

  .hero-actions {
    flex-direction: column;
    align-items: center;
  }

  .primary-action,
  .secondary-action {
    width: min(260px, 100%);
  }
}
</style>
