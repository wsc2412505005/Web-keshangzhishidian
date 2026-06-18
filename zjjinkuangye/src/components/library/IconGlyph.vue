<template>
  <svg class="icon-glyph" viewBox="0 0 24 24" aria-hidden="true">
    <template v-if="name === 'search'">
      <circle cx="11" cy="11" r="6.5" />
      <path d="m16 16 4.2 4.2" />
    </template>

    <template v-else-if="name === 'user'">
      <circle cx="12" cy="8" r="3.2" />
      <path d="M5.5 19.2c1.4-3.2 3.6-4.8 6.5-4.8s5.1 1.6 6.5 4.8" />
      <circle cx="12" cy="12" r="9.2" />
    </template>

    <template v-else-if="name === 'settings'">
      <path d="M12 8.2a3.8 3.8 0 1 0 0 7.6 3.8 3.8 0 0 0 0-7.6Z" />
      <path
        d="M19.4 14.6c.1-.5.2-1 .2-1.6s-.1-1.1-.2-1.6l2-1.5-2-3.4-2.4 1a8 8 0 0 0-2.7-1.6L14 3.3h-4l-.4 2.6a8 8 0 0 0-2.7 1.6l-2.4-1-2 3.4 2 1.5c-.1.5-.2 1-.2 1.6s.1 1.1.2 1.6l-2 1.5 2 3.4 2.4-1a8 8 0 0 0 2.7 1.6l.4 2.6h4l.4-2.6a8 8 0 0 0 2.7-1.6l2.4 1 2-3.4-2.1-1.5Z" />
    </template>

    <template v-else-if="name === 'filter'">
      <path d="M5 7h14" />
      <path d="M8 12h8" />
      <path d="M11 17h2" />
    </template>

    <template v-else-if="name === 'sort'">
      <path d="M7 7h10" />
      <path d="M7 12h7" />
      <path d="M7 17h4" />
    </template>

    <template v-else-if="name === 'clock'">
      <circle cx="12" cy="12" r="8.2" />
      <path d="M12 7.5v5l3.3 2" />
    </template>

    <template v-else-if="name === 'external'">
      <path d="M9 6H6.5A1.5 1.5 0 0 0 5 7.5v10A1.5 1.5 0 0 0 6.5 19h10a1.5 1.5 0 0 0 1.5-1.5V15" />
      <path d="M13 5h6v6" />
      <path d="m11 13 8-8" />
    </template>

    <template v-else-if="name === 'chevron-right'">
      <path d="m9 6 6 6-6 6" />
    </template>

    <template v-else-if="name === 'chevron-left'">
      <path d="m15 6-6 6 6 6" />
    </template>

    <template v-else-if="name === 'arrow-right'">
      <path d="M5 12h14" />
      <path d="m13 6 6 6-6 6" />
    </template>

    <template v-else-if="name === 'analytics'">
      <path d="M5 19V9" />
      <path d="M12 19V5" />
      <path d="M19 19v-7" />
    </template>
  </svg>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    required: true,
  },
})
</script>

<style scoped>
.icon-glyph {
  display: block;
  width: 1em;
  height: 1em;
  fill: none;
  stroke: currentColor;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-width: 1.7;
}
</style>
