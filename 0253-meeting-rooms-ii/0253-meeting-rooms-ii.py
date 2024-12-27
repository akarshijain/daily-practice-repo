class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_start_times = []
        meeting_end_times = []

        for start, end in intervals:
            meeting_start_times.append(start)
            meeting_end_times.append(end)

        meeting_start_times.sort()
        meeting_end_times.sort()

        index_s, index_e = 0, 0
        num_meetings, num_conference_rooms = 0, 0

        while index_s < len(meeting_start_times) \
            and index_e < len(meeting_end_times):
            if meeting_start_times[index_s] < meeting_end_times[index_e]:
                num_meetings += 1
                index_s += 1

            elif meeting_start_times[index_s] > meeting_end_times[index_e]:
                num_meetings -= 1
                index_e += 1

            else:
                num_meetings -= 1
                index_e += 1

            num_conference_rooms = max(num_conference_rooms, num_meetings)

        return num_conference_rooms