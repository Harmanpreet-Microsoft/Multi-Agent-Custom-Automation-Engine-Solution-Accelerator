import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
    Button,
    Text,
    Card,
    CardHeader
} from '@fluentui/react-components';
import {
    Add20Regular,
    ArrowLeft24Regular,
    ErrorCircle24Regular
} from '@fluentui/react-icons';
import '../styles/PlanPage.css';
import CoralShellColumn from '../coral/components/Layout/CoralShellColumn';
import CoralShellRow from '../coral/components/Layout/CoralShellRow';
import Content from '../coral/components/Content/Content';
import PanelLeft from '../coral/components/Panels/PanelLeft';
import PanelLeftToolbar from '../coral/components/Panels/PanelLeftToolbar';
import TaskList from '../components/content/TaskList';

/**
 * Page component for displaying a specific plan
 * Accessible via the route /plan/{plan_id}
 */
const PlanPage: React.FC = () => {
    const { planId } = useParams<{ planId: string }>();
    const navigate = useNavigate();

    // Temporary placeholder data - will be replaced with API calls
    const inProgressTasks: any[] = [];
    const completedTasks: any[] = [];

    // Handle back navigation
    const handleBackClick = () => {
        navigate(-1);
    };

    const handleTaskSelect = (taskId: string) => {
        console.log(`Selected task ID: ${taskId}`);
    };

    const handleNewTask = (taskName: string) => {
        console.log(`Creating new task: ${taskName}`);
    };

    // Show error if no planId is provided
    if (!planId) {
        return (
            <div style={{ padding: '20px' }}>
                <Text>Error: No plan ID provided</Text>
            </div>
        );
    }


    return (
        <CoralShellColumn>
            <CoralShellRow>
                <div style={{ flexShrink: 0, display: "flex", overflow: "hidden" }}>
                    <PanelLeft
                        panelWidth={280}
                        panelResize={true}>
                        <PanelLeftToolbar panelTitle="" panelIcon={null}>
                            <Button
                                icon={<Add20Regular />}
                                onClick={() => handleNewTask("New task")}
                            >
                                New task
                            </Button>
                        </PanelLeftToolbar>
                        <TaskList
                            inProgressTasks={inProgressTasks}
                            completedTasks={completedTasks}
                            onTaskSelect={handleTaskSelect}
                        />
                    </PanelLeft>
                    <Content>

                    </Content>
                </div>
            </CoralShellRow>
        </CoralShellColumn>
    );
};

export default PlanPage;