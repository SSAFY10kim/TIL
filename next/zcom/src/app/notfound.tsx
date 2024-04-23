import Link from 'next/link'
import {NextPage} from "next"

const NotFound: NextPage = () => {
  return (
    <div>
      <div>이 페이지는 존재하지 않습니다. 다른페이지를 검색해보세요.</div>
      <Link href="/search"></Link>
    </div>
  )
}

export default NotFound;