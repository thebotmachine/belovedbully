import type { Dog } from '~/types/dog'
import type { ComputedRef } from 'vue'

type Crumb = { label: string; to?: string }

const SECTION_MAP: Record<string, Crumb> = {
  puppies:   { label: 'Свободные щенки', to: '/puppies' },
  producers: { label: 'Производители',   to: '/producers' },
  graduates: { label: 'Выпускники',      to: '/graduates' },
}

const ROLE_TO_SECTION: Record<string, string> = {
  puppy:    'puppies',
  producer: 'producers',
  graduate: 'graduates',
}

export const useDogBreadcrumbs = (
  dog: ComputedRef<Dog | null>,
  from?: string
) => {
  return computed(() => {
    const crumbs: Crumb[] = [{ label: 'Главная', to: '/' }]
    if (!dog.value) return crumbs

    const { litter, role, name } = dog.value
    const useLitter = litter && (from === 'litters' || !from)

    if (useLitter) {
      crumbs.push({ label: 'Помёты', to: '/litters' })
      crumbs.push({ label: litter.name, to: `/litters/${litter.slug}` })
    } else {
      const sectionKey = from ?? ROLE_TO_SECTION[role.value]
      crumbs.push(SECTION_MAP[sectionKey] ?? { label: 'Собаки', to: '/dogs' })
    }

    crumbs.push({ label: name })
    return crumbs
  })
}