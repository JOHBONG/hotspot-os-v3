import Head from 'next/head'

export default function Home() {
  return (
    <div>
      <Head>
        <title>HotspotOS V3 Dashboard</title>
      </Head>
      <main className="flex min-h-screen items-center justify-center bg-gray-100">
        <div className="rounded-lg bg-white p-12 shadow-md text-center">
          <h1 className="text-3xl font-bold mb-2">Welcome to HotspotOS V3</h1>
          <p className="text-gray-600">Modern Hotspot Management for ISPs & Operators</p>
        </div>
      </main>
    </div>
  )
}
