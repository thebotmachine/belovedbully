import type {MaybeRefOrGetter} from 'vue'
import type {Dog} from '~/types/dog'


export const useDog = (
    slug: MaybeRefOrGetter<string>
) => {

    return useApi<Dog>(
        () => `/dogs/${toValue(slug)}/`,
        {
            key: () => `dog-${toValue(slug)}`,
        }
    )
}