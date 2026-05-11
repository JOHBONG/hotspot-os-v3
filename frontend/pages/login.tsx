import { useState } from 'react'
import Head from 'next/head'

export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [msg, setMsg] = useState('')

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setMsg('')
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    })
    const data = await res.json()
    if(res.ok) {
      setMsg('✔️ Login successful! Token: ' + data.access_token)
    } else {
      setMsg('❌ ' + (data.detail || 'Invalid credentials'))
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <Head><title>Login | HotspotOS V3</title></Head>
      <form onSubmit={handleLogin} className="bg-white shadow-md rounded p-8 max-w-md w-full">
        <h2 className="mb-6 text-2xl font-bold text-center">HotspotOS V3 Login</h2>
        <input type="text" autoFocus placeholder="Username" className="block w-full mb-4 px-4 py-2 border rounded" value={username} onChange={e => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" className="block w-full mb-6 px-4 py-2 border rounded" value={password} onChange={e => setPassword(e.target.value)} />
        <button type="submit" className="w-full py-2 bg-blue-600 text-white font-semibold rounded">Login</button>
        {msg && <div className="mt-4 text-center text-sm">{msg}</div>}
      </form>
    </div>
  )
}