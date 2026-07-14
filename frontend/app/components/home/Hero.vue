<script setup lang="ts">
function heroMotion(delay = 0) {
  return {
    initial: {
      scale: 1.1,
      opacity: 0,
      filter: 'blur(20px)'
    },
    animate: {
      scale: 1,
      opacity: 1,
      filter: 'blur(0px)'
    },
    transition: {
      duration: 0.8,
      delay
    }
  }
}
</script>

<template>
  <section
      class="relative isolate overflow-hidden min-h-[calc(100svh-var(--ui-header-height))]"
  >
    <img
        src="/hero1.jpg"
        alt="BelovedBully питомник"
        class="absolute inset-0 w-full h-full object-cover z-0"
    />

    <div
        class="absolute inset-0 z-10 bg-gradient-to-t
             from-[var(--ui-bg-inverted)]/90
             via-[var(--ui-bg-inverted)]/30
             to-transparent"
    />

    <div
        class="absolute inset-0 z-10 bg-gradient-to-r
             from-[var(--ui-bg-inverted)]/50
             to-transparent"
    />

    <div
        class="absolute bottom-0 left-0 right-0 h-80 z-10
             bg-gradient-to-t
             from-[var(--ui-bg-elevated)]
             via-[var(--ui-bg-elevated)]/70
             to-transparent"
    />

    <UContainer
        class="relative z-20 min-h-[calc(100svh-var(--ui-header-height))]
         flex flex-col justify-end pb-12 md:pb-20"
    >

      <div class="max-w-2xl">

        <div class="text-3xl md:text-6xl text-inverted font-serif tracking-normal">
          <Motion v-bind="heroMotion(0.1)">
            <span class="block">Добро</span>
          </Motion>

          <Motion v-bind="heroMotion(0.2)">
            <span class="block">пожаловать</span>
          </Motion>

          <Motion v-bind="heroMotion(0.3)">
            <span class="block">в питомник</span>
          </Motion>

          <Motion v-bind="heroMotion(0.4)">
            <span class="block">
              <em class="italic">BelovedBully</em>
            </span>
          </Motion>
        </div>

        <Motion v-bind="heroMotion(0.5)">
          <p class="mt-4 md: mt-6 sm:text-lg text-[var(--ui-color-neutral-200)]">
            В каждом щенке мы видим любовь!
          </p>
        </Motion>

        <Motion v-bind="heroMotion(0.6)">
          <div class="flex gap-4 mt-6 md: mt-8">
            <UButton
                to="/puppies"
                color="primary"
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
    </UContainer>
  </section>
</template>

<style scoped>

</style>