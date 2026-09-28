// Adapted from shadcn/studio @ss-blocks/blog-component-01 (grid of cards with image, title, description, actions).
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardTitle, CardDescription, CardHeader } from '@/components/ui/card'

export type Theme = {
  slug: string
  name: string
  description: string
  kind: string
  brief: string
  demo: string
  playground: string
  source: string
  shot: string
}

const ThemesGrid = ({ themes }: { themes: Theme[] }) => {
  return (
    <section className='pb-16 lg:pb-24'>
      <div className='mx-auto max-w-7xl px-4 sm:px-6 lg:px-8'>
        <div className='grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3'>
          {themes.map(theme => (
            <Card className='pt-0' key={theme.slug}>
              <CardContent className='px-0'>
                <a href={theme.demo}>
                  <img
                    src={theme.shot}
                    alt={`Home page of the ${theme.name} theme`}
                    loading='lazy'
                    className='aspect-[4/3] w-full rounded-t-xl object-cover object-top'
                  />
                </a>
              </CardContent>
              <CardHeader className='flex h-full flex-col justify-between gap-6'>
                <div className='space-y-2'>
                  <p className='text-muted-foreground text-sm'>{theme.kind}</p>
                  <CardTitle className='text-xl font-semibold'>
                    <a href={theme.demo}>{theme.name}</a>
                  </CardTitle>
                  <CardDescription className='text-base'>{theme.description}</CardDescription>
                </div>
                <div className='flex flex-wrap gap-2'>
                  <Button size='lg' render={<a href={theme.demo} />} nativeButton={false}>
                    Demo
                  </Button>
                  <Button size='lg' variant='outline' render={<a href={theme.playground} />} nativeButton={false}>
                    Try in Playground
                  </Button>
                  <Button size='lg' variant='ghost' render={<a href={theme.source} />} nativeButton={false}>
                    Source
                  </Button>
                </div>
              </CardHeader>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}

export default ThemesGrid
