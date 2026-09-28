// Adapted from shadcn/studio @ss-blocks/footer-component-01 (brand row, links, separator, note).
import { Separator } from '@/components/ui/separator'

const SiteFooter = () => {
  return (
    <footer>
      <Separator />
      <div className='mx-auto flex max-w-7xl items-center justify-between gap-3 px-4 py-6 max-md:flex-col sm:px-6 md:py-8 lg:px-8'>
        <span className='font-semibold'>Open WP themes</span>
        <div className='flex items-center gap-5 whitespace-nowrap'>
          <a href='https://github.com/sampler321/wp-oss' className='opacity-80 transition-opacity duration-300 hover:opacity-100'>
            GitHub
          </a>
          <a href='https://wposs-themes.b-j-kapica.workers.dev' className='opacity-80 transition-opacity duration-300 hover:opacity-100'>
            All 50 themes
          </a>
        </div>
      </div>
      <Separator />
      <div className='mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8'>
        <p className='text-muted-foreground text-sm text-balance'>
          Demo sites are static snapshots. Try in Playground boots the real theme with its demo content in your
          browser, editor included. Demo images are CC0 or public domain, credited in each theme's readme.
        </p>
      </div>
    </footer>
  )
}

export default SiteFooter
