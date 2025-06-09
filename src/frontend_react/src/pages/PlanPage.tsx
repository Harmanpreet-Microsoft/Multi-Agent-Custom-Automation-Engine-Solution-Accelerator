import React, { useCallback, useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
    Button,
    Text,
    Card,
    CardHeader,
    useToastController,
    Spinner,
    Badge
} from '@fluentui/react-components';
import {
    Add20Regular,
    ArrowLeft24Regular,
    ErrorCircle24Regular,
    Person24Regular,
    CheckmarkCircle24Regular,
    AlertUrgent24Regular,
    Sparkle20Filled
} from '@fluentui/react-icons';
import '../styles/PlanPage.css';
import CoralShellColumn from '../coral/components/Layout/CoralShellColumn';
import CoralShellRow from '../coral/components/Layout/CoralShellRow';
import Content from '../coral/components/Content/Content';
import PanelLeft from '../coral/components/Panels/PanelLeft';
import PanelLeftToolbar from '../coral/components/Panels/PanelLeftToolbar';
import TaskList from '../components/content/TaskList';
import { NewTaskService } from '../services/NewTaskService';
import { PlanDataService, ProcessedPlanData } from '../services/PlanDataService';
import { PlanWithSteps, Task, AgentType, Step } from '@/models';
import { apiService } from '@/api';
import PlanPanelLeft from '@/components/content/PlanPanelLeft';
import ContentToolbar from '@/coral/components/Content/ContentToolbar';
import Chat from '@/coral/modules/Chat';
import TaskDetails from '@/components/content/TaskDetails';
import PlanChat from '@/components/content/PlanChat';

/**
 * Page component for displaying a specific plan
 * Accessible via the route /plan/{plan_id}
 */
const PlanPage: React.FC = () => {
    const { planId } = useParams<{ planId: string }>();
    const navigate = useNavigate();

    // State for plan data
    const [planData, setPlanData] = useState<ProcessedPlanData | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<Error | null>(null);
    const handleOnchatSubmit = useCallback(() => {
        NewTaskService.handleNewTaskFromHome();
    }, []);

    const handleApproveStep = useCallback((step: Step) => {
        NewTaskService.handleNewTaskFromHome();
    }, []);

    const handleRejectStep = useCallback((step: Step) => {
        NewTaskService.handleNewTaskFromHome();
    }, []);
    /**
     * Fetch plan data when component mounts or planId changes
     */
    const loadPlanData = useCallback(async () => {
        if (!planId) return;

        try {
            setLoading(true);
            setError(null);

            const data = await PlanDataService.fetchPlanData(planId);
            console.log('Fetched plan data:', data);
            setPlanData(data);
        } catch (err) {
            console.error('Failed to load plan data:', err);
            setError(err instanceof Error ? err : new Error('Failed to load plan data'));
        } finally {
            setLoading(false);
        }
    }, [planId]);

    // Load plan data on mount and when planId changes
    useEffect(() => {
        loadPlanData();
    }, [loadPlanData]);

    const handleNewTaskButton = () => {
        // Use NewTaskService to handle navigation to homepage and reset textarea
        NewTaskService.handleNewTaskFromPlan(navigate);
    };    // Show error if no planId is provided
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
                <PlanPanelLeft onNewTaskButton={handleNewTaskButton} />
                <Content>
                    <ContentToolbar
                        panelTitle={planData?.plan?.initial_goal || 'Plan Details'}
                        panelIcon={<Sparkle20Filled />}
                    ></ContentToolbar>
                    <PlanChat
                        PlanData={planData}
                        OnChatSubmit={handleOnchatSubmit}
                    />
                    <TaskDetails
                        PlanData={planData}
                        OnApproveStep={handleApproveStep}
                        OnRejectStep={handleRejectStep}
                    />

                </Content>
            </CoralShellRow>
        </CoralShellColumn>
    );


};

export default PlanPage;