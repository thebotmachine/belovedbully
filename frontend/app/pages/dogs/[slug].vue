<script setup lang="ts">
const route = useRoute()
const slug = computed(() => route.params.slug as string)

const {data: dog, pending, error} = await useDog(slug)

const {formatDate, formatAge} = useFormatDate()

useSeoMeta({
  title: () => `${dog.value.name}`,
  description: () => ``,
});


const breadcrumbItems = useDogBreadcrumbs(
    computed(() => dog.value ?? null),
    route.query.from as string | undefined
)

interface Media {
  id: number
  url: string
  alt?: string
  title?: string
}

const isOpen = ref(false)
const selectedMedia = ref<Media | null>(null)

function openModal(media: Media) {
  selectedMedia.value = media
  isOpen.value = true
}
</script>

<template>
  <div class="bg-elevated">
    <UContainer class="py-8">
      <UBreadcrumb :items="breadcrumbItems" class="mb-8"/>

      <div v-if="pending">Загрузка...</div>

      <div v-else-if="error">Не удалось загрузить собаку.</div>

      <div v-else-if="dog"
           class="bg-default border-b-3 border-accented ring-1 ring-accented/40 shadow-lg rounded-xl p-4">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">

          <div class="relative aspect-square overflow-hidden bg-muted rounded-lg">
            <img
                v-if="dog.cover"
                :src="dog.cover.medium_url"
                alt="Product illustration"
                loading="lazy"
                class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
            />
            <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
          </div>

          <div class="space-y-4">

            <h1 class="text-5xl leading-tight font-medium text-balance font-serif">{{ dog.name }}</h1>
            <div class="flex flex-wrap items-center gap-2 text-toned">
              <UBadge color="neutral" variant="outline">{{ dog.status.label }}</UBadge>
              <div>
                <UBadge color="neutral" variant="outline">{{ dog.gender.label }}</UBadge>
              </div>
              <UBadge color="neutral" variant="outline">{{ formatAge(dog.birth_date) }}</UBadge>
            </div>
            <p class="max-w-prose text-muted leading-relaxed ">{{ dog.description }}</p>


            <div class="bg-muted rounded-xl p-4 leading-relaxed space-y-2">
              <div class="flex justify-between">
                <div class="text-muted">Дата рождения</div>
                <div class="font-medium">{{ formatDate(dog.birth_date) }}</div>
              </div>

              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between">
                <div class="text-muted">Пол</div>
                <div class="font-medium">{{ dog.gender.label }}</div>
              </div>

              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between">
                <div class="text-muted">Размер</div>
                <div class="font-medium">{{ dog.size.label }}</div>
              </div>

              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between">
                <div class="text-muted">Окрас</div>
                <div class="font-medium">{{ dog.color.label }}</div>
              </div>

              <div v-if="dog.litter" class="bg-elevated rounded-xl p-4 space-y-2 -mx-4 -mb-4">
                <div class="flex justify-between">
                  <div class="text-muted">Мать</div>
                  <ULink
                      :to="`/dogs/${dog.litter.mother.slug}`"
                      raw
                      class="group font-medium flex items-center gap-1 hover:text-neutral-700 transition-colors"
                  >
                    {{ dog.litter.mother.name }}
                    <UIcon
                        name="i-lucide-chevron-right"
                        class="size-4 transition-transform duration-300 group-hover:translate-x-1"
                    />
                  </ULink>
                </div>

                <USeparator :ui="{ border: 'border-accented' }"/>

                <div class="flex justify-between">
                  <div class="text-muted">Отец</div>
                  <ULink
                      :to="`/dogs/${dog.litter.father.slug}`"
                      raw
                      class="group font-medium flex items-center gap-1 hover:text-neutral-700 transition-colors"
                  >
                    {{ dog.litter.father.name }}
                    <UIcon
                        name="i-lucide-chevron-right"
                        class="size-4 transition-transform duration-300 group-hover:translate-x-1"
                    />
                  </ULink>
                </div>

                <USeparator :ui="{ border: 'border-accented' }"/>

                <div class="flex justify-between">
                  <div class="text-muted">Помёт</div>
                  <div class="font-medium">
                    <ULink
                        :to="`/litters/${dog.litter.slug}`"
                        raw
                        class="group font-medium flex items-center gap-1 hover:text-neutral-700 transition-colors"
                    >
                      {{ dog.litter.name }}
                      <UIcon
                          name="i-lucide-chevron-right"
                          class="size-4 transition-transform duration-300 group-hover:translate-x-1"
                      />
                    </ULink>
                  </div>
                </div>
              </div>
            </div>

            <div class="flex flex-col md:flex-row gap-2">
              <UButton block size="xl" color="neutral" variant="outline">Родословная</UButton>
              <UButton block size="xl" color="neutral">Забронировать</UButton>
            </div>

          </div>

        </div>

        <div class="">
          <div class="text-center py-8 text-4xl italic leading-tight font-medium text-balance font-serif">Фотографии
          </div>
          <div class="columns-2 gap-2 md:gap-4 lg:columns-3 xl:columns-4">

            <div
                v-for="media in dog.media"
                :key="media.id"
                class="break-inside-avoid mb-2 md:mb-4 overflow-hidden rounded-lg group cursor-pointer"
                @click="openModal(media)"
            >
              <img
                  :src="media.medium_url"
                  :alt="media.alt || 'Product illustration'"
                  loading="lazy"
                  class="w-full object-cover transition-transform duration-700 group-hover:scale-105"
              />
            </div>


            <UModal
                v-model:open="isOpen"
                fullscreen
                :ui="{
                      content: 'bg-transparent',
                      header: 'hidden',
                      footer: 'hidden',
                      body: 'p-0 h-full',
                  }"

            >
              <template #body>
                <div class="w-full h-full flex items-center justify-center" @click="isOpen = false">
                  <img
                      v-if="selectedMedia"
                      :src="selectedMedia.large_url"
                      class="max-h-[85vh] max-w-[85vw] object-contain rounded-xl cursor-default"
                      @click.stop
                      alt="Просмотр"
                  />
                </div>
                <UButton
                    icon="i-lucide-x"
                    color="neutral"
                    variant="subtle"
                    size="xl"
                    class="absolute top-4 right-4 z-50"
                    @click="isOpen = false"
                />
              </template>
            </UModal>


          </div>
        </div>

      </div>
    </UContainer>
  </div>
</template>
