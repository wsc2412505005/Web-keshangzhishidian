<template>
  <section class="visual-section" id="analysis">
    <div class="visual-inner">
      <!-- Left side text content -->
      <div class="visual-copy">
        <span class="section-label">合规可视化引擎 | VISUALIZATION ENGINE</span>
        <h2>把合规文本转成可读的业务判断</h2>
        <p>
          平台不仅是静态展示资料，还会围绕地区、业务环节、风险等级和关键词进行多维度关联，
          帮助用户秒懂跨境合规文本之间的联系与潜在风险。
        </p>

        <ul class="feature-list">
          <li class="feature-item">
            <span class="checkmark-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="checkmark-icon">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </span>
            <div class="feature-text">
              <h4>智能关联索引</h4>
              <p>按国家、地区和业务环节建立全球文本深度索引</p>
            </div>
          </li>
          <li class="feature-item">
            <span class="checkmark-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="checkmark-icon">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </span>
            <div class="feature-text">
              <h4>核心实体抽取</h4>
              <p>精准提取高频关键词，形成智能化分类与合规要点</p>
            </div>
          </li>
          <li class="feature-item">
            <span class="checkmark-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="checkmark-icon">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </span>
            <div class="feature-text">
              <h4>多维直观洞察</h4>
              <p>以图形化看板展示风险等级、资料类型与关键词热图</p>
            </div>
          </li>
        </ul>

        <div class="action-btn-group">
          <RouterLink to="/library" class="explore-btn">
            探索可视化引擎
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-arrow">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </RouterLink>
        </div>
      </div>

      <!-- Right side dashboard preview & floating card -->
      <div class="visual-frame">
        <div class="dashboard-card glass-card">
          <div class="card-inner">
            <img 
              src="https://lh3.googleusercontent.com/aida-public/AB6AXuBFlEnsesFFuIj3sf-WhQFBH_Kj2mtC7G5GYyxp3r6cT9fJ3eQ2aFh5fibExWgkN3tvHaAw_8Up4v_VImnfffagW64KMWu1voWhhGNLUCyKLoLteTYW0XnHqFECx7X_qzEMFD2mlz4UbnV90PO7LfoKAhSqhqGsHoLLYOGW6nyD-mpBj123qgd2Uyr8rRugjlGGsqA62Q5kELg9brMtN0gLqWN27KN5VUG_pPf02E9gmvz95_Eqj2YOjcm8d6Ufa3ApVw6Y5wEuzazS" 
              alt="Data Dashboard Visualization" 
              class="dashboard-img"
            />
            <div class="stream-overlay">
              <div class="stream-bar glass-card">
                <div class="status-indicator">
                  <span class="pulse-dot"></span>
                  <span class="status-text">全球合规文献流式处理中...</span>
                </div>
                <span class="live-tag">LIVE</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Floating Decorative Card -->
        <div class="floating-card glass-card animate-float">
          <div class="floating-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="node-svg">
              <circle cx="12" cy="12" r="3"></circle>
              <circle cx="6" cy="6" r="3"></circle>
              <circle cx="18" cy="6" r="3"></circle>
              <circle cx="18" cy="18" r="3"></circle>
              <circle cx="6" cy="18" r="3"></circle>
              <line x1="6" y1="6" x2="12" y2="12"></line>
              <line x1="18" y1="6" x2="12" y2="12"></line>
              <line x1="18" y1="18" x2="12" y2="12"></line>
              <line x1="6" y1="18" x2="12" y2="12"></line>
            </svg>
          </div>
          <div class="floating-meta">
            <strong>关联节点 analysis</strong>
            <span>Node Analysis</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.visual-section {
  position: relative;
  overflow: hidden;
  padding: 118px clamp(20px, 5vw, 64px);
  background:
    radial-gradient(circle at 8% 20%, rgba(255, 255, 255, 0.02), transparent 32%),
    radial-gradient(circle at 82% 52%, rgba(255, 255, 255, 0.04), transparent 34%),
    #111111;
  color: var(--color-text);
}

.visual-section::before {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px);
  background-size: 72px 72px;
  mask-image: linear-gradient(180deg, transparent, #000 12%, #000 88%, transparent);
  content: "";
}

.visual-inner {
  display: grid;
  max-width: 1240px;
  margin: 0 auto;
  grid-template-columns: minmax(0, 0.95fr) minmax(420px, 1.05fr);
  gap: clamp(48px, 6vw, 92px);
  align-items: center;
}

.visual-copy .section-label {
  display: inline-block;
  color: var(--color-gold);
  font-size: 13px;
  font-weight: 900;
  letter-spacing: 0.08em;
  margin-bottom: 12px;
}

.visual-copy h2 {
  max-width: 560px;
  margin: 0 0 20px;
  font-family: var(--font-sans);
  font-size: clamp(32px, 4vw, 48px);
  font-weight: 850;
  line-height: 1.16;
  color: #fffaf0;
  text-shadow: 0 10px 30px rgba(0, 0, 0, 0.24);
}

.visual-copy p {
  max-width: 560px;
  margin: 0 0 34px;
  color: var(--color-muted);
  font-size: 17px;
  line-height: 1.8;
}

.feature-list {
  display: grid;
  gap: 26px;
  margin: 0 0 42px;
  padding: 0;
  list-style: none;
}

.feature-item {
  display: flex;
  gap: 18px;
  align-items: flex-start;
}

.checkmark-wrapper {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--color-gold);
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.14);
}

.checkmark-icon {
  width: 14px;
  height: 14px;
}

.feature-text h4 {
  margin: 0 0 6px;
  font-size: 17px;
  font-weight: 900;
  color: var(--color-text);
  letter-spacing: 0.02em;
}

.feature-text p {
  margin: 0;
  font-size: 14px;
  color: var(--color-muted);
  line-height: 1.55;
}

.explore-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 52px;
  padding: 0 28px;
  border-radius: 999px;
  border: 2px solid rgba(255, 255, 255, 0.18);
  background: rgba(255, 255, 255, 0.03);
  color: #f5efe2;
  font-size: 14px;
  font-weight: 950;
  text-decoration: none;
  box-shadow: none;
  transition: all 0.35s var(--ease-premium);
}

.explore-btn:hover {
  transform: translateY(-2px);
  border-color: var(--color-gold);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 12px 34px rgba(255, 255, 255, 0.05);
  color: #fff;
}

.btn-arrow {
  width: 16px;
  height: 16px;
  transition: transform 0.35s var(--ease-premium);
}

.explore-btn:hover .btn-arrow {
  transform: translateX(4px);
}

/* Right-side visual frame styling */
.visual-frame {
  position: relative;
  width: 100%;
}

.dashboard-card {
  position: relative;
  overflow: hidden;
  border-radius: 18px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(20, 20, 20, 0.38);
  box-shadow: 0 42px 110px rgba(0, 0, 0, 0.52);
  padding: 12px;
  transition:
    border-color 0.45s var(--ease-premium),
    box-shadow 0.45s var(--ease-premium);
}

.dashboard-card:hover {
  border-color: rgba(255, 255, 255, 0.25);
  box-shadow: 0 52px 130px rgba(0, 0, 0, 0.62);
}

.card-inner {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  width: 100%;
  aspect-ratio: 4 / 3.4;
}

.dashboard-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
  filter: saturate(0.85) contrast(1.05);
  transition:
    transform 0.8s cubic-bezier(0.25, 1, 0.3, 1),
    filter 0.8s var(--ease-premium);
}

.dashboard-card:hover .dashboard-img {
  transform: scale(1.04);
  filter: saturate(1.05) contrast(1.1);
}

.stream-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20px;
  background: linear-gradient(180deg, transparent 0%, rgba(0, 0, 0, 0.88) 100%);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  z-index: 3;
}

.stream-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  width: 100%;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(20, 20, 20, 0.74);
  backdrop-filter: blur(14px);
  box-shadow: 0 12px 38px rgba(0, 0, 0, 0.24);
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 10px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-gold);
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.12);
  animation: white-pulse 2s infinite;
}

.status-text {
  font-size: 11px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.74);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.live-tag {
  font-size: 11px;
  font-weight: 900;
  color: var(--color-gold);
  letter-spacing: 0.08em;
  animation: flash-live 2.5s infinite;
}

/* Floating Card style with smooth hover scaling and bounce keyframes */
.floating-card {
  position: absolute;
  top: -14px;
  right: -14px;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px 22px;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  background: rgba(20, 20, 20, 0.86);
  backdrop-filter: blur(18px);
  box-shadow: 0 22px 58px rgba(0, 0, 0, 0.38);
  transition:
    border-color 0.35s var(--ease-premium),
    transform 0.35s var(--ease-premium);
}

.floating-card:hover {
  border-color: var(--color-gold);
  transform: translateY(-4px) scale(1.02) !important;
}

.floating-icon {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--color-gold);
  flex-shrink: 0;
}

.node-svg {
  width: 20px;
  height: 20px;
  animation: node-spin 20s linear infinite;
}

.floating-meta {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.floating-meta strong {
  font-size: 13px;
  font-weight: 900;
  color: var(--color-text);
  letter-spacing: 0.02em;
}

.floating-meta span {
  font-size: 9px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.44);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-top: 2px;
}

/* Animations */
@keyframes white-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.3);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(255, 255, 255, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
  }
}

@keyframes flash-live {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}

@keyframes node-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.animate-float {
  animation: float-y 5s ease-in-out infinite;
}

@keyframes float-y {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0px);
  }
}

@media (max-width: 980px) {
  .visual-inner {
    grid-template-columns: 1fr;
    gap: 56px;
  }
}

@media (max-width: 640px) {
  .visual-section {
    padding: 72px 18px;
  }

  .floating-card {
    display: none;
  }

  .stream-bar {
    padding: 0 12px;
  }

  .status-text {
    font-size: 9px;
  }
}
</style>
