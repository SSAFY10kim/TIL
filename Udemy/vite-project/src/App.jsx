import { useState } from 'react'
import TabButton from './components/TabButton'

function App() {
  const [tabContent, setTabContent] = useState("Please Click a button")

  function handleClick(e) {
    setTabContent(e)

  }

  return (
    <div>
      <h1>Hello World!</h1>
      <section>
        <menu>
          <TabButton onSelect={() => handleClick('Components')}>
            Components
          </TabButton>
          <TabButton onSelect={() => handleClick('JSX')}>
            JSX
          </TabButton>
          <TabButton onSelect={() => handleClick('Props')}>
            Props
          </TabButton>
          <TabButton onSelect={() => handleClick('State')}>
            State
          </TabButton>
        </menu>
        {tabContent}
      </section>
    </div>
  )
}

export default App
