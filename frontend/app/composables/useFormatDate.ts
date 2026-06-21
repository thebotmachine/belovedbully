export const useFormatDate = () => {
  const formatDate = (date: string | Date): string =>
    new Date(date)
      .toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
      .replace(' г.', '')

  const formatAge = (date: string | Date): string => {
    const birth = new Date(date)
    const now = new Date()

    const months =
      (now.getFullYear() - birth.getFullYear()) * 12 +
      (now.getMonth() - birth.getMonth())

    if (months < 1) return 'Менее месяца'
    if (months < 12) return `${months} ${pluralize(months, 'месяц', 'месяца', 'месяцев')}`

    const years = Math.floor(months / 12)
    const rem = months % 12

    const yearStr = `${years} ${pluralize(years, 'год', 'года', 'лет')}`
    const monthStr = rem ? ` ${rem} ${pluralize(rem, 'месяц', 'месяца', 'месяцев')}` : ''

    return yearStr + monthStr
  }

  return { formatDate, formatAge }
}

const pluralize = (n: number, one: string, few: string, many: string): string => {
  const mod10 = n % 10
  const mod100 = n % 100

  if (mod100 >= 11 && mod100 <= 19) return many
  if (mod10 === 1) return one
  if (mod10 >= 2 && mod10 <= 4) return few
  return many
}