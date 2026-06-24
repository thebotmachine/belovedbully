<script setup lang="ts">
import {stagger} from 'motion-v'

defineProps<{
  title: string
  subtitle: string
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
  <div class="flex flex-col items-center justify-center gap-2">
    <Motion
        tag="h2"
        :initial="{ opacity: 0, y: 40 }"
        :whileInView="{ opacity: 1, y: 0 }"
        :transition="{ duration: 0.7, delay: 0.2 }"
        :inViewOptions="{ once: true, amount: 0.2 }"
        class="text-3xl sm:text-4xl lg:text-5xl text-pretty tracking-tight text-highlighted font-serif"
    >
      {{ title }}
    </Motion>
    <Motion
        tag="p"
        :initial="{ opacity: 0, y: 30 }"
        :whileInView="{ opacity: 1, y: 0 }"
        :transition="{ duration: 0.6, delay: 0.5 }"
        :inViewOptions="{ once: true, amount: 0.2 }"
        class="sm:text-lg text-toned text-center"
    >
      {{ subtitle }}
    </Motion>
  </div>

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
        :items="dogs"
        arrows
        :ui="{ item: 'basis-[70%] p-4 gap-1' }"
        class="mx-auto max-w-sm"
    >
      <Motion
          tag="div"
          :variants="cardVariants"
          initial="hidden"
          whileInView="visible"
          :inViewOptions="{ once: true, amount: 0.3 }"
      >
        <DogsCard :dog="item" :fromContext="fromContext"/>
      </Motion>
    </UCarousel>
  </div>

  <div class="flex justify-center mt-6">
    <UButton :to="to" color="neutral" size="lg" trailing-icon="i-lucide-chevron-right">
      Смотреть еще
    </UButton>
  </div>
</template>