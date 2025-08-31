<h1>Day 14  - Largest 3-Same-Digit Number in String</h1>

<p><strong>Problem Link:</strong><br>
  <a href="https://leetcode.com/problems/largest-3-same-digit-number-in-string/" target="_blank" rel="noopener noreferrer">
    LeetCode 2264 - Largest 3-Same-Digit Number in String
  </a>
</p>

<hr>

<p>
  You are given a string <code>num</code> representing a large integer.<br>
  An integer is called <strong>good</strong> if it satisfies:
</p>
<ol>
  <li>It is a <strong>substring</strong> of <code>num</code> with <strong>length 3</strong>.</li>
  <li>It consists of <strong>only one unique digit</strong>.</li>
</ol>

<p>
  Return the <strong>maximum good integer</strong> as a string, or an empty string <code>""</code> if no such integer exists.
</p>

<hr>

<h3>Rules:</h3>
<ul>
  <li>The substring must have <strong>exactly 3</strong> characters.</li>
  <li>All three characters must be the <strong>same digit</strong>.</li>
  <li><strong>Leading zeroes</strong> are allowed.</li>
  <li>If multiple good integers exist, return the <strong>largest</strong> one (by numeric value).</li>
</ul>

<hr>

<h3>Return:</h3>
<ul>
  <li>The <strong>maximum good integer</strong> as a string.</li>
  <li>If none exists, return <code>""</code>.</li>
</ul>

<hr>

<h3>Example 1:</h3>
<pre><code><strong>Input:</strong>
num = "6777133339"

<strong>Output:</strong>
"777"

<strong>Explanation:</strong>
Possible good integers: "777" and "333".
"777" is larger, so we return it.
</code></pre>

<h3>Example 2:</h3>
<pre><code><strong>Input:</strong>
num = "2300019"

<strong>Output:</strong>
"000"

<strong>Explanation:</strong>
Only "000" is a valid good integer.
</code></pre>

<h3>Example 3:</h3>
<pre><code><strong>Input:</strong>
num = "42352338"

<strong>Output:</strong>
""

<strong>Explanation:</strong>
No substring of length 3 consists of the same digit.
</code></pre>

<hr>

