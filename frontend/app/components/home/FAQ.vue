<template>
  <UAccordion :items="items" :ui="uiConfig">
    <!-- Переопределяем слот для контента аккордеона -->
    <template #default="{ item, index, open }">
      <div class="border-b border-gray-200 dark:border-gray-700">
        <!-- Кнопка-триггер (стандартный дизайн) -->
        <UButton
          color="gray"
          variant="ghost"
          class="w-full justify-between px-4 py-4 text-left font-medium"
          :ui="{ rounded: 'rounded-none' }"
          @click="toggle(index)"
        >
          <span>{{ item.label }}</span>
          <UIcon
            name="i-heroicons-chevron-right-20-solid"
            class="w-5 h-5 transition-transform duration-200"
            :class="{ 'rotate-90': open }"
          />
        </UButton>

        <!-- Анимированный контент с Motion -->
        <AnimatePresence mode="wait">
          <motion.div
            v-if="open"
            :key="`${index}-content`"
            :initial="initialState"
            :animate="animateState"
            :exit="exitState"
            :transition="transition"
            class="overflow-hidden will-change-transform"
          >
            <div class="px-4 pb-4 pt-2 text-gray-600 dark:text-gray-300">
              {{ item.content }}
            </div>
          </motion.div>
        </AnimatePresence>
      </div>
    </template>
  </UAccordion>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { AnimatePresence, motion } from 'motion-v'

// Пропсы компонента
const props = defineProps<{
  items: Array<{ label: string; content: string }>
}>()

// Состояние открытых элементов (индексы)
const openIndices = ref<number[]>([])

const toggle = (index: number) => {
  const idx = openIndices.value.indexOf(index)
  if (idx === -1) {
    openIndices.value.push(index)
  } else {
    openIndices.value.splice(idx, 1)
  }
}

// Стандартная конфигурация UI (без изменений)
const uiConfig = {
  wrapper: 'space-y-0 divide-y divide-gray-200 dark:divide-gray-800',
  item: 'relative',
}

// Motion-анимации
const initialState = {
  opacity: 0,
  height: 0,
  filter: 'blur(6px)',
}

const animateState = {
  opacity: 1,
  height: 'auto',
  filter: 'blur(0px)',
}

const exitState = {
  opacity: 0,
  height: 0,
  filter: 'blur(6px)',
}

const transition = {
  type: 'tween',
  duration: 0.4,
  ease: [0.25, 0.1, 0.25, 1], // элегантная кривая
  opacity: { duration: 0.3 },
  filter: { duration: 0.3 },
}
</script>