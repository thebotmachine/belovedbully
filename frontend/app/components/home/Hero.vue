<script setup lang="ts">

</script>

<template>
<div class="relative min-h-screen overflow-hidden bg-transparent">
    <img
        src="/compressed_image.jpeg"
        alt="BelovedBully питомник"
        loading="eager"
        class="absolute inset-0 h-full w-full object-cover bg-fixed"
    />

    <div
        class="absolute inset-0 z-[2] bg-gradient-to-t from-[var(--ui-bg-inverted)]/90 via-[var(--ui-bg-inverted)]/30 to-transparent"/>
    <div class="absolute inset-0 z-[2] bg-gradient-to-r from-[var(--ui-bg-inverted)]/50 to-transparent"/>
    <div
        class="absolute bottom-0 left-0 right-0 h-80 z-[4]
           bg-gradient-to-t
           from-[var(--ui-bg-elevated)]
           via-[var(--ui-bg-elevated)]/70
           to-transparent"
    />


    <div
        class="absolute inset-0 z-10 flex flex-col items-start justify-end max-w-(--ui-container) mx-auto px-4 sm:px-6 lg:px-8 pb-32 space-y-6 md:space-y-10"
    >
      <Motion
          :initial="{
        scale: 1.1,
        opacity: 0,
        filter: 'blur(20px)'
      }"
          :animate="{
        scale: 1,
        opacity: 1,
        filter: 'blur(0px)'
      }"
          :transition="{
        duration: 0.8,
        delay: 0.1
      }"
      >
        <div class="text-3xl md:text-6xl text-inverted font-serif tracking-normal">
          <span class="block">Добро пожаловать</span>
          <span class="block">в питомник</span>
          <span class="block">
          <em class="italic">BelovedBully</em>
        </span>
        </div>
      </Motion>

      <Motion
          :initial="{
        scale: 1.1,
        opacity: 0,
        filter: 'blur(20px)'
      }"
          :animate="{
        scale: 1,
        opacity: 1,
        filter: 'blur(0px)'
      }"
          :transition="{
        duration: 0.8,
        delay: 0.3
      }"
      >
        <p class="sm:text-lg text-[var(--ui-color-neutral-200)]">
          В каждом щенке мы видим любовь!
        </p>
      </Motion>

      <Motion
          :initial="{
        scale: 1.1,
        opacity: 0,
        filter: 'blur(20px)'
      }"
          :animate="{
        scale: 1,
        opacity: 1,
        filter: 'blur(0px)'
      }"
          :transition="{
        duration: 0.8,
        delay: 0.5
      }"
      >
        <div class="flex gap-4">
          <UButton
              to="/puppies"
              color="neutral"
              variant="solid"
              size="xl"
              trailing-icon="i-lucide-chevron-right"
              class="bg-default hover:bg-default/75 active:bg-default/50 text-default"
          >
            Свободные щенки
          </UButton>
        </div>
      </Motion>
    </div>
  </div>
</template>

<style scoped>

</style>