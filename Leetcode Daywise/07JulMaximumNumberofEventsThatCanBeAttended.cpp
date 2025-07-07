#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        // Sort events by start day
        sort(events.begin(), events.end());
        
        priority_queue<int, vector<int>, greater<int>> minHeap; // min-heap to store end days

        int day = 1, i = 0, n = events.size(), count = 0;
        
        // Loop until we've either processed all events or there are no more attendable events
        while (i < n || !minHeap.empty()) {
            // If heap is empty, jump to the next event's start day
            if (minHeap.empty()) {
                day = events[i][0];
            }

            // Add all events that start today
            while (i < n && events[i][0] == day) {
                minHeap.push(events[i][1]); // add endDay
                i++;
            }

            // Remove events that have already expired (end day < current day)
            while (!minHeap.empty() && minHeap.top() < day) {
                minHeap.pop();
            }

            // Attend the event that ends the earliest
            if (!minHeap.empty()) {
                minHeap.pop(); // attend event
                count++;
                day++; // move to next day
            }
        }

        return count;
    }
};
