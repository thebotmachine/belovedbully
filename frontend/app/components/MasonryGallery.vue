<script setup lang="ts">
import { watch } from 'vue'

export interface GalleryImage {
  id: string | number
  url: string
  alt: string
}

defineProps<{
  images: GalleryImage[]
}>()

const isOpen = ref(false)
const selectedImage = ref<GalleryImage | null>(null)

function openModal(image: GalleryImage) {
  selectedImage.value = image
  isOpen.value = true
}

watch(isOpen, (open) => {
  if (!open) {
    selectedImage.value = null
  }
})

function getMasonryClass(index: number) {
  const bigIndices = [1, 5, 10, 15]
  const verticalIndices = [3, 7, 12, 18]
  const horizontalIndices = [0, 4, 9, 14, 19]

  if (bigIndices.includes(index)) return 'big'
  if (verticalIndices.includes(index)) return 'vertical'
  if (horizontalIndices.includes(index)) return 'horizontal'

  return ''
}
</script>

<template>
  <div class="w-full">
    <div class="masonry-grid">
      <button
        v-for="(image, index) in images"
        :key="image.id"
        type="button"
        class="masonry-item group relative overflow-hidden rounded-lg focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-500"
        :class="getMasonryClass(index)"
        :aria-label="`Open image: ${image.alt}`"
        @click="openModal(image)"
      >
        <img
          :src="image.url"
          :alt="image.alt"
          loading="lazy"
          class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110"
        />

        <div
          class="absolute inset-0 bg-black/40 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
        />
      </button>
    </div>

    <UModal
  v-model:open="isOpen"
  fullscreen
  :close="false"
>
  <div class="relative flex h-full items-center justify-center">
    <UButton
      icon="i-heroicons-x-mark"
      color="neutral"
      variant="ghost"
      class="absolute top-4 right-4 z-50"
      @click="isOpen = false"
    />

    <img
      v-if="selectedImage"
      :src="selectedImage.url"
      :alt="selectedImage.alt"
      class="max-w-[90vw] max-h-[90vh] object-contain"
    />
  </div>
</UModal>
  </div>
</template>

<style scoped>
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: 150px;
  grid-auto-flow: dense;
  gap: .5rem;
}

.masonry-item.horizontal {
  grid-column: span 2;
}

.masonry-item.vertical {
  grid-row: span 2;
}

.masonry-item.big {
  grid-column: span 2;
  grid-row: span 2;
}

@media (max-width:640px) {
  .masonry-grid {
    grid-template-columns: repeat(2,1fr);
    grid-auto-rows:120px;
  }

  .masonry-item.horizontal,
  .masonry-item.big {
    grid-column: span 2;
  }

  .masonry-item.vertical {
    grid-row: span 2;
  }
}
</style>