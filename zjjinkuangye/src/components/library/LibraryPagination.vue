<template>
  <nav v-if="totalPages > 1" class="pagination" aria-label="Document pagination">
    <button type="button" :disabled="currentPage === 1" aria-label="Previous page"
      @click="$emit('change', currentPage - 1)">
      <IconGlyph name="chevron-left" />
    </button>

    <button v-for="page in pages" :key="page" type="button" :class="{ 'is-active': page === currentPage }"
      @click="$emit('change', page)">
      {{ page }}
    </button>

    <button type="button" :disabled="currentPage === totalPages" aria-label="Next page"
      @click="$emit('change', currentPage + 1)">
      <IconGlyph name="chevron-right" />
    </button>
  </nav>
</template>

<script setup>
import { computed } from 'vue'
import IconGlyph from './IconGlyph.vue'

const props = defineProps({
  currentPage: {
    type: Number,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true,
  },
})

defineEmits(['change'])

const pages = computed(() => {
  return Array.from({ length: props.totalPages }, (_, index) => index + 1)
})
</script>

<style scoped>
.pagination {
  display: flex;
  width: fit-content;
  align-items: center;
  gap: 8px;
  margin: 56px auto 0;
  padding: 8px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.04);
}

button {
  display: grid;
  width: 40px;
  height: 40px;
  place-items: center;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: rgba(255, 255, 255, 0.74);
  cursor: pointer;
  font-size: 14px;
  font-weight: 900;
  transition:
    background 0.3s var(--ease-premium),
    color 0.3s var(--ease-premium),
    transform 0.3s var(--ease-premium);
}

button:hover:not(:disabled),
button.is-active {
  background: #ffffff;
  color: #090d16;
  transform: translateY(-1px);
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.34;
}

.icon-glyph {
  font-size: 18px;
}
</style>
