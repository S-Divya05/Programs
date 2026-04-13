class Solution {
    public int lengthOfLongestSubstring(String s) {
       int[] visited = new int[256];   // ASCII characters
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {

            // If character already exists, shrink window
            while (visited[s.charAt(right)] == 1) {
                visited[s.charAt(left)] = 0;
                left++;
            }

            // Mark current character
            visited[s.charAt(right)] = 1;

            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
    
}
