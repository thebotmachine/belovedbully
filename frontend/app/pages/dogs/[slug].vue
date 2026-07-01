<script setup lang="ts">
const route = useRoute()
const slug = computed(() => route.params.slug as string)

const {data: dog, pending, error} = useDog(slug)

const {formatDate, formatAge} = useFormatDate()

useSeoMeta({
  title: () => dog.value?.name ?? 'Собака',
  description: () => '',
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


const galleryHeights = ['h-72', 'h-48', 'h-64', 'h-56', 'h-80', 'h-40', 'h-60', 'h-52']
</script>

<template>
  <div class="bg-elevated">
    <UContainer class="py-8">
      <UBreadcrumb :items="breadcrumbItems" class="mb-8"/>

      <div
          v-if="pending"
          class="bg-default border-b-3 border-accented ring-1 ring-accented/40 shadow-lg rounded-xl p-4"
      >
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">

          <USkeleton class="aspect-square w-full rounded-lg"/>

          <div class="space-y-4">

            <USkeleton class="h-11 w-2/3 rounded-md"/>

            <div class="flex flex-wrap items-center gap-2">
              <USkeleton class="h-6 w-20 rounded-full"/>
              <USkeleton class="h-6 w-24 rounded-full"/>
              <USkeleton class="h-6 w-16 rounded-full"/>
            </div>


            <div class="space-y-2 max-w-prose">
              <USkeleton class="h-4 w-full"/>
              <USkeleton class="h-4 w-full"/>
              <USkeleton class="h-4 w-3/4"/>
            </div>


            <div class="bg-muted rounded-xl p-4 space-y-3">
              <div class="flex justify-between items-center">
                <USkeleton class="h-4 w-28"/>
                <USkeleton class="h-4 w-20"/>
              </div>
              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between items-center">
                <USkeleton class="h-4 w-16"/>
                <USkeleton class="h-4 w-20"/>
              </div>
              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between items-center">
                <USkeleton class="h-4 w-20"/>
                <USkeleton class="h-4 w-16"/>
              </div>
              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between items-center">
                <USkeleton class="h-4 w-16"/>
                <USkeleton class="h-4 w-24"/>
              </div>
            </div>


            <div class="flex flex-col md:flex-row gap-2">
              <USkeleton class="h-12 w-full rounded-md"/>
              <USkeleton class="h-12 w-full rounded-md"/>
            </div>

          </div>
        </div>


        <div>
          <div class="flex justify-center py-8">
            <USkeleton class="h-10 w-56 rounded-md"/>
          </div>
          <div class="columns-2 gap-2 md:gap-4 lg:columns-3 xl:columns-4">
            <USkeleton
                v-for="(h, i) in galleryHeights"
                :key="i"
                class="break-inside-avoid mb-2 md:mb-4 w-full rounded-lg"
                :class="h"
            />
          </div>
        </div>
      </div>

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