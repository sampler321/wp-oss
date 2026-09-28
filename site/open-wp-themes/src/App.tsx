import ThemesGrid, { type Theme } from '@/components/site/themes-grid'
import SiteFooter from '@/components/site/site-footer'
import themes from '@/data/themes.json'

const App = () => {
  return (
    <div className='bg-background text-foreground min-h-screen'>
      <header className='mx-auto max-w-7xl px-4 pt-12 pb-8 sm:px-6 lg:px-8'>
        <h1 className='text-5xl font-bold leading-none tracking-tight sm:text-7xl'>
          Open WP themes
        </h1>
        <p className='text-muted-foreground mt-6 text-sm'>GPL-2.0 / WordPress 6.7+</p>
      </header>
      <ThemesGrid themes={themes as Theme[]} />
      <SiteFooter />
    </div>
  )
}

export default App
