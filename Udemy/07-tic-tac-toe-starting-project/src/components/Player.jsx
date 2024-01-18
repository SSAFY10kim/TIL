import { useState } from "react"

export default function Player({ name, symbol, isActive }) {
  const [isEditing, setIsEditing] = useState(false)
  const [playerName, setPlayerName] = useState(name)

  function handleEditClick() {
    setIsEditing((editing) => !editing)
  }

  function handleChange(event) {
    setPlayerName(event.target.value)
  }

  return (
    <li className={isActive ? 'active' : undefined}>
      <span className='player'>
        {isEditing ?
          <input type="text" required value={playerName} onChange={handleChange} /> :
          <span className='player-name'>{playerName}</span>
        }
        <span className='player-symbol'>{symbol}</span>
      </span>

      <button onClick={handleEditClick}>{isEditing ? 'Save' : 'Edit'}</button>
    </li>
  )
}