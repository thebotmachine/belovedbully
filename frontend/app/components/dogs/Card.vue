<script setup lang="ts">
import type {Dog, DogListItem} from '~/types/dog'


const props = defineProps<{
  dog: DogListItem
  fromContext?: string
}>()

const {formatAge} = useFormatDate()


const to = computed(() => {
  const base = `/dogs/${props.dog.slug}`
  if (props.fromContext) {
    return {
      path: base,
      query: {from: props.fromContext}
    }
  }
  return base
})


</script>

<template>
    <NuxtLink :to="to">
      <div
          class="group overflow-hidden rounded-xl border-b-3 border-accented bg-default md:shadow-md ring-1 ring-accented/20 md:duration-300 md:hover:shadow-lg md:hover:ring-accented/80 md:transition-color">
        <div class="relative aspect-square overflow-hidden bg-muted">
          <img
              v-if="dog.cover"
              :src="dog.cover.medium_url"
              alt="Dog Photo"
              loading="lazy"
              class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
          />
          <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
        </div>

        <div class="p-3 md:p-4 space-y-1 md:space-y-2 text-center">
          <h3 class="text-2xl md:text-3xl font-medium font-serif">
            {{ dog.name }}
          </h3>
          <div class="flex flex-col md:flex-row items-center justify-between text-muted text-sm md:text-base">
            <p>{{ dog.gender.label }}</p>
            <p>{{ formatAge(dog.birth_date) }}</p>
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