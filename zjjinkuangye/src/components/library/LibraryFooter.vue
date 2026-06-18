<template>
  <footer class="library-footer">
    <div class="footer-inner">
      <div>
        <strong>三亚紫金矿业</strong>
        <p>通过公开文献采集与监管合规大数据，赋能跨国矿业全流程合规安全运营。</p>
      </div>

      <nav aria-label="页脚导航">
        <a href="#">隐私政策</a>
        <a href="#">服务条款</a>
        <a href="#">合规指引</a>
        <a href="#">技术支持</a>
      </nav>
    </div>

    <p class="copyright">© 2026 三亚紫金矿业跨境合规文本展示平台. 保留所有权利.</p>
  </footer>
</template>

<style scoped>
.library-footer {
  position: relative;
  z-index: 1;
  border-top: 1px solid rgba(245, 239, 226, 0.1);
  background: rgba(6, 8, 7, 0.92);
  color: var(--color-text);
}

.footer-inner {
  display: flex;
  width: min(1440px, calc(100% - 48px));
  margin: 0 auto;
  justify-content: space-between;
  align-items: anchor-center;
  gap: 42px;
  padding: 54px 0 40px;
}

strong {
  display: block;
  font-size: 18px;
  font-weight: 950;
}

p {
  max-width: 440px;
  margin: 12px 0 0;
  color: var(--color-muted);
  font-size: 15px;
  line-height: 1.65;
}

nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 24px;
}

a {
  color: rgba(245, 239, 226, 0.68);
  font-size: 14px;
  font-weight: 850;
  text-decoration: none;
}

a:hover {
  color: var(--color-gold);
}

.copyright {
  width: min(1440px, calc(100% - 48px));
  max-width: none;
  margin: 0 auto;
  padding: 28px 0 42px;
  border-top: 1px solid rgba(245, 239, 226, 0.08);
  text-align: center;
}

@media (max-width: 780px) {
  .footer-inner {
    display: grid;
  }

  nav {
    justify-content: flex-start;
  }

  .copyright {
    text-align: left;
  }
}
</style>
