import ThemesGrid, { type Theme } from '@/components/site/themes-grid'
import SiteFooter from '@/components/site/site-footer'
import { Separator } from '@/components/ui/separator'
import themes from '@/data/themes.json'

const App = () => {
  return (
    <div className='bg-background text-foreground min-h-screen'>
      <header className='mx-auto max-w-7xl px-4 pt-12 pb-8 sm:px-6 lg:px-8'>
        <h1 className='text-5xl font-bold leading-none tracking-tight sm:text-7xl'>
          Open WP
          <br />
          themes
        </h1>
        <p className='text-muted-foreground mt-6 max-w-2xl text-lg'>
          {themes.length} free, open-source WordPress block themes for small businesses, makers and creatives. Every theme
          uses core blocks only, and every colour, font and size lives in theme.json, so it can all be changed in the
          Site Editor.
        </p>
        <p className='text-muted-foreground mt-2 text-sm'>
          GPL-2.0-or-later, WordPress 6.7 or newer, source on{' '}
          <a className='underline underline-offset-4' href='https://github.com/sampler321/wp-oss'>
            github.com/sampler321/wp-oss
          </a>
        </p>
      </header>
      <Separator className='mx-auto mb-10 max-w-7xl' />
      <ThemesGrid themes={themes as Theme[]} />
      <SiteFooter />
    </div>
  )
}

export default App
