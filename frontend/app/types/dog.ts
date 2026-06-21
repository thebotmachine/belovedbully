interface DogField {
    value: string | number
    label: string
}


export type DogGender = 'male' | 'female'


export interface DogListItem {
  slug: string
  name: string
  birth_date: string
  gender: {
    value: 'male' | 'female'
    label: string
  }
}

export interface Dog {
    id: number
    slug: string
    name: string
    description: string
    birth_date: string
    gender: DogField & { value: DogGender }
    status: DogField
    role: DogField
    size: DogField
    color: DogField
    litter: null
}


export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}