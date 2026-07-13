<script setup lang="ts">
import {stagger} from 'motion-v'

defineProps<{
  dogs: Dog[]
  fromContext: 'puppies' | 'producers'
  to: string
}>()

const gridVariants = {
  hidden: {},
  visible: {
    transition: {
      delayChildren: stagger(0.30),
      when: "beforeChildren",
    },
  },
}

const cardVariants = {
  hidden: {opacity: 0, y: 24, scale: 0.98, filter: "blur(4px)"},
  visible: {
    opacity: 1, y: 0, scale: 1, filter: "blur(0px)",
    transition: {duration: 0.7, ease: "easeOut"},
  },
}
</script>

<template>
  <Motion
      v-if="dogs.length"
      tag="div"
      :variants="gridVariants"
      initial="hidden"
      whileInView="visible"
      :inViewOptions="{ once: true, amount: 0.2 }"
      class="hidden md:grid grid-cols-4 gap-4"
  >
    <Motion
        v-for="dog in dogs"
        :key="dog.slug"
        tag="div"
        :variants="cardVariants"
    >
      <DogsCard :dog="dog" :fromContext="fromContext"/>
    </Motion>
  </Motion>

  <div class="overflow-hidden w-full md:hidden">
    <UCarousel
        v-if="dogs.length"
        v-slot="{ item }"
        class-names
        :items="dogs"
        arrows
        :ui="{ item: 'basis-[45%] gap-1 ' }"
        class="mx-auto max-w-sm"
    >
        <DogsCard :dog="item" :fromContext="fromContext"/>
    </UCarousel>
  </div>

  <div class="flex justify-center mt-6">
    <UButton :to="to" color="neutral" size="lg" trailing-icon="i-lucide-chevron-right">
      Смотреть еще
    </UButton>
  </div>
</template>