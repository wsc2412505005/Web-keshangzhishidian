<template>
  <footer class="home-footer">
    <div>
      <strong>紫金合规文本平台</strong>
      <p>面向课程项目的跨境矿业合规文本采集、分析与可视化展示原型。</p>
    </div>

    <nav aria-label="页脚导航">
      <RouterLink to="/">首页</RouterLink>
      <RouterLink to="/library">文本资料库</RouterLink>
      <a href="#analysis">文本分析</a>
      <a href="#about">项目说明</a>
    </nav>

    <small>2026 Sanya Zijin Mining Cross-border Compliance Platform</small>
  </footer>
</template>

<style scoped>
.home-footer {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 32px;
  align-items: center;
  padding: 40px clamp(20px, 5vw, 64px);
  border-top: 1px solid var(--color-line);
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.015), transparent 52%),
    #000000;
  color: var(--color-text);
}

strong {
  display: block;
  font-size: 18px;
}

p {
  margin: 8px 0 0;
  color: var(--color-muted);
}

nav {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

a {
  color: rgba(245, 239, 226, 0.68);
  font-weight: 800;
  text-decoration: none;
  transition:
    color 0.28s var(--ease-premium),
    opacity 0.28s var(--ease-premium);
}

a:hover {
  color: var(--color-gold);
}

small {
  color: rgba(245, 239, 226, 0.48);
  text-align: right;
}

@media (max-width: 900px) {
  .home-footer {
    grid-template-columns: 1fr;
  }

  small {
    text-align: left;
  }
}
</style>
