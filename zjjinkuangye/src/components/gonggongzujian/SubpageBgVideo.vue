<template>
  <div class="subpage-bg-video" aria-hidden="true">
    <video class="video-element" autoplay loop muted playsinline :src="src"></video>
    <div class="video-overlay"></div>
  </div>
</template>

<script setup>
// 公共副页视频背景组件：通过 src 属性支持自定义视频源，默认回退为文献库专属科技视频地址
defineProps({
  src: {
    type: String,
    required: true,
  },
})
</script>

<style scoped>
.subpage-bg-video {
  position: fixed;
  inset: 0;
  z-index: 0;
  /* 设为 0 以防被 body/html 根背景遮挡，且依然能完美居于内容（z-index: 1/10）底层 */
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  background: #000000;
  /* 提供固定的纯黑暗夜底托 */
}

.video-element {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.38;
  /* 调高至 0.38 保证视频在各种屏幕上都清晰可见，同时保持暗夜质感 */
}

.video-overlay {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 12% 0%, rgba(255, 255, 255, 0.03), transparent 30%),
    radial-gradient(circle at 88% 8%, rgba(255, 255, 255, 0.015), transparent 34%),
    linear-gradient(180deg, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.15) 38%, rgba(0, 0, 0, 0.8) 100%);
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .video-element {
    display: none;
    /* 完美兼容无障碍动效减弱模式 */
  }
}
</style>
