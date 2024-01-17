import { useState } from 'react'
import TabButton from './components/TabButton'
import { EXAMPLES } from './data.js'

function App() {
  const [tabContent, setTabContent] = useState("")

  function handleClick(e) {
    setTabContent(e)
  }

  return (
    <div>
      <h1>Hello World!</h1>
      <section>
        <menu>
          <TabButton
            isSelected={tabContent === 'components'}
            onSelect={() => handleClick('components')}>
            Components
          </TabButton>
          <TabButton
            isSelected={tabContent === 'jsx'}
            onSelect={() => handleClick('jsx')}>
            JSX
          </TabButton>
          <TabButton
            isSelected={tabContent === 'props'}
            onSelect={() => handleClick('props')}>
            Props
          </TabButton>
          <TabButton
            isSelected={tabContent === 'state'}
            onSelect={() => handleClick('state')}>
            State
          </TabButton>
        </menu>

        {!tabContent && <p>Please select a topic.</p>}
        {tabContent &&
          <div id="tab-content">
            <h3>{EXAMPLES[tabContent].title}</h3>
            <p>{EXAMPLES[tabContent].description}</p>
            <pre>
              <code>
                {EXAMPLES[tabContent].code}
              </code>
            </pre>
          </div>
        }
      </section>
    </div>
  )
}

export default App
