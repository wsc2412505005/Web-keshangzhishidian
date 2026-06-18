<template>
  <section class="hero-video" aria-label="首页视频背景">
    <Swiper class="video-swiper" :modules="modules" effect="fade" :loop="true" :speed="1200"
      :autoplay="{ delay: 5200, disableOnInteraction: false }">
      <SwiperSlide v-for="slide in slides" :key="slide.src">
        <video class="background-video" autoplay muted loop playsinline preload="metadata">
          <source :src="slide.src" type="video/mp4" />
        </video>
      </SwiperSlide>
    </Swiper>
  </section>
</template>

<script setup>
import { Autoplay, EffectFade } from 'swiper/modules'
import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/effect-fade'

defineProps({
  slides: {
    type: Array,
    required: true,
  },
})

const modules = [Autoplay, EffectFade]
</script>

<style scoped>
.hero-video,
.video-swiper,
:deep(.swiper-wrapper),
:deep(.swiper-slide) {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.hero-video {
  z-index: 1;
}

.background-video {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1.02);
}
</style>
