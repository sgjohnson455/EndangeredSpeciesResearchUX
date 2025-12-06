import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0);
  const [array, setArray] = useState([]);
  // newUser
  const [newUser, setNewUser] = useState("");

  const fetchAPI = async () => {
    // access backend url
    const response = await axios.get("http://localhost:8080/api/users")
    //console.log(response.data.users)

    // collects api data from users
    setArray(response.data.users);
  }

  const addUser = async () => {
    if (!newUser.trim()) return;

    await axios.post("http://localhost:8080/api/users", {
      user: newUser
    });

    setNewUser("") // clears input for new user
    fetchAPI(); // reloads the newly updated list
  }

  useEffect(() => {
    fetchAPI()
  }, []);

  return (
    <>
      {/* <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div> */}
      <h1>User List</h1>
      <input
        type="text"
        placeholder="Add user"
        value={newUser}
        onChange={(e) => setNewUser(e.target.value)}
      />

      <div className="card">

        <button onClick={addUser}>
          Add User
        </button>
        {array.map((user, index) => (
          <div key={index}>
            <span>{user}</span><br></br>
          </div>
        ))}
      </div >
    </>
  )
}

export default App
