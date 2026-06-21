import type { MaybeRefOrGetter } from 'vue'
import type { Litter } from '~/types/litter'

export const useLitter = (
  slug: MaybeRefOrGetter<string>
) => {

  return useApi<Litter>(
    () => `/litters/${toValue(slug)}/`,
    {
      key: () => `litter-${toValue(slug)}`,
    }
  )
}