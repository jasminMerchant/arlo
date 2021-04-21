import React, { useState } from 'react'
import { Button } from '@blueprintjs/core'

const copy = (text: string) => {
  let success = false
  try {
    // Create container for the HTML
    const container = document.createElement('div')
    container.innerHTML = text

    // Hide element
    container.style.position = 'fixed'
    container.style.pointerEvents = 'none'
    container.style.opacity = '0'

    // Mount the container to the DOM to make `contentWindow` available
    document.body.appendChild(container)

    // Copy to clipboard
    window.getSelection()!.removeAllRanges()

    const range = document.createRange()
    range.selectNode(container)
    window.getSelection()!.addRange(range)

    const successful = document.execCommand('copy')
    if (!successful) {
      throw new Error('copy command was unsuccessful')
    }
    success = true

    // Remove the container
    document.body.removeChild(container)
  } catch (err) {
    console.log(err)
    success = false
  }
  return success
}

const CopyToClipboard = ({ getText }: { getText: () => string }) => {
  const [copied, setCopied] = useState(false)
  return (
    <Button
      icon={copied ? 'tick-circle' : 'clipboard'}
      onClick={() => {
        const success = copy(getText())
        if (success) {
          setCopied(true)
          setTimeout(() => setCopied(false), 3000)
        }
      }}
      style={{ width: '160px' }}
    >
      {copied ? 'Copied' : 'Copy to clipboard'}
    </Button>
  )
}

export default CopyToClipboard
