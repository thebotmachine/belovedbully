<script setup lang="ts">
import type {Litter} from '~/types/litter'


defineProps<{
  litter: Litter
}>()

const {formatDate} = useFormatDate()

</script>

<template>
  <NuxtLink :to="`/litters/${litter.slug}`">
    <div
        class="group overflow-hidden rounded-xl border-b-3 border-accented bg-default shadow-md ring-1 ring-accented/20 duration-300 hover:shadow-lg hover:ring-accented/80 transition-color">
      <div class="relative aspect-square overflow-hidden bg-muted">
        <img
            v-if="litter.medium_url"
            :src="litter.medium_url"
            alt="Product illustration"
            loading="lazy"
            class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
        />
        <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
      </div>

      <div class="p-3 md:p-4 space-y-1 md:space-y-2 text-center">
        <div class="relative">
          <h3 class="relative font-serif text-2xl md:text-3xl font-medium text-balance z-10">
            {{ litter.mother.name ?? 'Не указан' }}
          </h3>
          <h3 class="relative font-serif text-2xl md:text-3xl font-medium text-balance z-10">
            {{ litter.father.name ?? 'Не указана' }}
          </h3>

          <div
              class="absolute inset-0 -top-0 flex items-center justify-center italic font-serif text-4xl text-muted/20 z-0">
            x
          </div>
        </div>
        <div class="flex flex-col md:flex-row items-center justify-between text-muted text-sm md:text-base">
          <p>{{ litter.puppies_count }} щенков</p>
          <p>{{ formatDate(litter.birth_date) }}</p>
        </div>
        <UButton block color="neutral" variant="solid" class="mt-2">
          Подробнее
        </UButton>
      </div>
    </div>
  </NuxtLink>

</template>

<style scoped>

</style>