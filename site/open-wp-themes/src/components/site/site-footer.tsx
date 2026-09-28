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
        </div>
      </div>
    </footer>
  )
}

export default SiteFooter
